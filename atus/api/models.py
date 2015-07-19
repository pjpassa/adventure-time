from django.db import models
from jsonfield import JSONField
import django_filters


class Respondent(models.Model):
    tu_case_id = models.CharField(max_length=25)
    statistical_weight = models.FloatField()
    variables = JSONField()
    activity_time_spent = JSONField(blank=True)

    @property
    def get_url(self):
        return "http://127.0.0.1:8000/respondents/{}/".format(self.id)