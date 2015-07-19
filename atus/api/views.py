from statistics import mean
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from api.models import Respondent
import django_filters


class RespondentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respondent
        fields = ["tu_case_id", "statistical_weight", "variables", "activity_time_spent"]


class RespondentListSerializer(serializers.ModelSerializer):

    url = serializers.URLField(source="get_url")

    class Meta:
        model = Respondent
        fields = ["url", "tu_case_id"]


class ActivityDetailSerializer(serializers.ModelSerializer):

    activity_code = serializers.CharField(max_length=7)
    average_minutes = serializers.FloatField(default=0)

    class Meta:
        model = Respondent
        fields = ["activity_code", "average_minutes"]


class RespondentDetailView(RetrieveAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentDetailSerializer


class RespondentListView(ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentListSerializer


class ActivityDetailView(GenericAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentDetailSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        avg = weighted_average_minutes(queryset, self.kwargs[self.lookup_field])
        obj = {"activity_code": self.kwargs[self.lookup_field],
               "average_minutes": avg}
        return Response(obj)

    def get(self, request, pk, format=None):
        return self.get_object()


def weighted_average_minutes(data, activity_code):
    weight = 0
    weighted_minutes = 0
    for instance in data:
        weight += instance.statistical_weight
        weighted_minutes += instance.statistical_weight * int(instance.activity_time_spent[activity_code])
    if weight == 0:
        return -1
    return weighted_minutes / weight