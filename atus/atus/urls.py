from django.conf.urls import include, url
from django.contrib import admin
from api import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'$', views.home_view),
    url(r'^respondent/(?P<pk>\d+)/$', views.RespondentDetailView.as_view(), name="respondent_detail"),
    url(r'^respondent/$', views.RespondentListView.as_view(), name="respondent_list"),
    url(r'^activities/(?P<pk>\d+)/$', views.ActivityView.as_view(), name="activity"),
    url(r'^respondents/(?P<pk>\d+)/', views.RespondentDetailView.as_view(), name="respondent_detail"),
    url(r'^respondents/$', views.RespondentListView.as_view(), name="respondent_list"),
    url(r'^activity/(?P<pk>t\d{6})/', views.ActivityDetailView.as_view(), name="activity_detail"),
]
