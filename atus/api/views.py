
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.models import Respondent
import django_filters


class RespondentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respondent
        fields = ["id", "tu_case_id", "statistical_weight", "variables", "activity_time_spent"]


class RespondentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respondent
        fields = ["id", "tu_case_id"]


class RespondentDetailView(RetrieveAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentDetailSerializer


class RespondentListView(ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentListSerializer
