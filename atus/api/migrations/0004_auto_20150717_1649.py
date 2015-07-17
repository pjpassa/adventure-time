# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.db import models, migrations
from api.models import Respondent


def load_summary_data(x, y):
    with open("../data/atussum_2014/atussum_2014.dat") as file:
        data = csv.DictReader(file)
        for line in data:
            resp = Respondent.objects.get_or_create(tu_case_id=line.pop("tucaseid"))[0]
            resp.activity_time_spent = line
            resp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150717_1639'),
    ]

    operations = [
        migrations.RunPython(load_summary_data)
    ]
