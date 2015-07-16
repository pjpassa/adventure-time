from django.db import models
from jsonfield import JSONField

# Create your models here.
class Respondent(models.Model):
    statistical_weight = models.FloatField()
    variables = JSONField()


class TimeSpent(models.Model):
    respondent = models.ForeignKey(Respondent)
    activity = models.CharField(max_length=7)
    activity_label = models.CharField(max_length=100)
    time_spent = models.IntegerField()