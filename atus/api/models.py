from django.db import models
from jsonfield import JSONField
import django_filters


class Respondent(models.Model):
    tu_case_id = models.CharField(max_length=25)
    statistical_weight = models.FloatField()
    variables = JSONField()
    activity_time_spent = JSONField(blank=True)


class TimeSpent(models.Model):
    respondent = models.ForeignKey(Respondent, related_name="time_spent")
    activity = models.CharField(max_length=7)
    activity_label = models.CharField(max_length=100)
    time_spent = models.IntegerField()


"""class TimesSpentFilter(django_filters.FilterSet):
    # You can set up a filter on a model based on the fields.

    class Meta:
        model = TimeSpent
        fields = ["respondent", "activity", "activity_label", "time_spent"]
# can set up a filter by passing a dictionary to the fields attribute.
        # also have an order_by attribute to control the display
        fields = {'price': ['lt', 'gt'],
                  'release_date': ['exact'],"""

