# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(verbose_name='Index')),
                ('value', models.PositiveIntegerField(verbose_name='Value')),
                ('weight', models.PositiveIntegerField(verbose_name='Weight')),
            ],
            options={
                'verbose_name': 'Input item',
                'verbose_name_plural': 'Input items',
                'ordering': ('task', 'index'),
            },
        ),
        migrations.CreateModel(
            name='KSTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(blank=True, null=True, verbose_name='Task ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='Start time')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='End time')),
                ('capacity', models.PositiveIntegerField(verbose_name='Capacity')),
                ('value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'KnapSack task',
                'verbose_name_plural': 'KnapSack tasks',
            },
        ),
        migrations.CreateModel(
            name='ResultItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(verbose_name='Index')),
                ('value', models.PositiveIntegerField(verbose_name='Value')),
                ('weight', models.PositiveIntegerField(verbose_name='Weight')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='ks.KSTask')),
            ],
            options={
                'verbose_name': 'Result item',
                'verbose_name_plural': 'Result items',
                'ordering': ('task', 'index'),
            },
        ),
        migrations.AddField(
            model_name='inputitem',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ks.KSTask'),
        ),
    ]