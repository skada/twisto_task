# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ks.models import KSTask, InputItem, ResultItem


class BaseItemInline(admin.TabularInline):
    fields = ('index', 'value', 'weight')
    can_delete = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    readonly_fields = ('index', 'value', 'weight')


class InputItemInline(BaseItemInline):
    model = InputItem


class ResultItemInline(BaseItemInline):
    model = ResultItem


@admin.register(KSTask)
class KSTaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'resolver_method', 'start_time', 'end_time', )
    readonly_fields = ('task_id', 'start_time', 'end_time', 'capacity', 'value', 'resolver_method')
    inlines = (ResultItemInline, InputItemInline, )
    fieldsets = (
        (_('Task base info'), {
            'fields': ('task_id', ('capacity', 'value'), ('start_time', 'end_time'), 'resolver_method')
        }),
    )

