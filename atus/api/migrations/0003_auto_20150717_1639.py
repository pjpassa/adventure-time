# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import json
from django.core import serializers

from django.db import models, migrations
import jsonfield.fields
from api.models import Respondent


def load_respondent_data(x, y):
    with open("../data/atusresp_2014/atusresp_2014.dat") as file:
        data = csv.DictReader(file)
        for line in data:
            Respondent.objects.create(tu_case_id=line.pop("TUCASEID"),
                                             statistical_weight=line.pop("TUFINLWGT"),
                                             variables=line)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_respondent_activity_time_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respondent',
            name='activity_time_spent',
            field=jsonfield.fields.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='timespent',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent', related_name='time_spent'),
        ),
        migrations.AddField(
            model_name='respondent',
            name='tu_case_id',
            field=models.CharField(max_length=25, default=0),
            preserve_default=False,
        ),
       migrations.RunPython(load_respondent_data)
    ]
