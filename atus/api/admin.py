from django.contrib import admin

# Register your models here.
from api.models import Respondent, TimeSpent

admin.site.register(Respondent)
admin.site.register(TimeSpent)
