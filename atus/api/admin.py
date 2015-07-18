from django.contrib import admin

# Register your models here.
from api.models import Respondent

admin.site.register(Respondent)
admin.site.register(TimeSpent)
