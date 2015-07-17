# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('statistical_weight', models.FloatField()),
                ('variables', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSpent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('activity', models.CharField(max_length=7)),
                ('activity_label', models.CharField(max_length=100)),
                ('time_spent', models.IntegerField()),
                ('respondent', models.ForeignKey(to='api.Respondent')),
            ],
        ),
    ]
