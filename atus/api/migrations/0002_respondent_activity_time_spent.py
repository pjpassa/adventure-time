# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondent',
            name='activity_time_spent',
            field=jsonfield.fields.JSONField(default=0),
            preserve_default=False,
        ),
    ]
