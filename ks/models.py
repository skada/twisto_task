# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.base import ModelBase
from django.utils import six
from django.utils.six import add_metaclass
from django.utils.translation import ugettext_lazy as _

from knapsack import celery_app
from ks.tasks import resolver_choices


class SackItem(models.Model):
    index = models.PositiveIntegerField(_('Index'))
    value = models.PositiveIntegerField(_('Value'))
    weight = models.PositiveIntegerField(_('Weight'))

    class Meta:
        abstract = True


class KSTask(models.Model):

    task_id = models.UUIDField(_('Task ID'), blank=True, null=True)
    start_time = models.DateTimeField(_('Start time'), auto_now_add=True)
    end_time = models.DateTimeField(_('End time'), blank=True, null=True)
    capacity = models.PositiveIntegerField(_('Capacity'))
    value = models.PositiveIntegerField(_('Value'), blank=True, null=True)
    resolver_method = models.CharField(_('Resolver method'), max_length=50, choices=resolver_choices,
                                       default=resolver_choices.default_resolver)

    @property
    def num_items(self):
        return len(self.items.all())

    class Meta:
        verbose_name = _('KnapSack task')
        verbose_name_plural = _('KnapSack tasks')


class InputItem(SackItem):
    task = models.ForeignKey(KSTask, related_name='items')

    class Meta:
        ordering = ('task', 'index')
        verbose_name = _('Input item')
        verbose_name_plural = _('Input items')


class ResultItem(SackItem):
    task = models.ForeignKey(KSTask, related_name='results')

    class Meta:
        ordering = ('task', 'index')
        verbose_name = _('Result item')
        verbose_name_plural = _('Result items')