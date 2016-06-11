# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 20:29
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

from spbgti_core import fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', fields.PairField(choices=[('1', 'Первая'), ('2', 'Вторая'), ('3', 'Третья'), ('4', 'Четвертая'), ('5', 'Пятая'), ('6', 'Шестая'), ('7', 'Седьмая')], default=1, max_length=1, verbose_name='Номер пары')),
                ('day', fields.DayOfTheWeekField(choices=[('1', 'Понедельник'), ('2', 'Вторник'), ('3', 'Среда'), ('4', 'Четверг'), ('5', 'Пятница'), ('6', 'Суббота'), ('7', 'Воскресенье')], default=1, max_length=1, verbose_name='День недели')),
                ('class_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название занятия')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место проведения')),
                ('teacher', models.CharField(blank=True, max_length=100, null=True, verbose_name='Преподаватель')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField(verbose_name='Номер группы')),
                ('year', models.DateField(default=django.utils.timezone.now, verbose_name='Год')),
                ('semester', models.IntegerField(verbose_name='Номер семестра')),
            ],
        ),
        migrations.AddField(
            model_name='classrecord',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Schedule'),
        ),
    ]