# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def load_respondent_data(x, y):
    raise BaseException()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_respondent_activity_time_spent'),
    ]

    operations = [
        migrations.RunPython(load_respondent_data)
    ]
