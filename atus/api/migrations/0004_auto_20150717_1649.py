# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def load_summary_data(x, y):
    raise BaseException()



class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150717_1639'),
    ]

    operations = [
        migrations.RunPython(load_summary_data)
    ]
