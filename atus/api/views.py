
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.models import Respondent, TimeSpent
import django_filters


class TimespentSerializer(serializers.ModelSerializer):


    class Meta:
        model = TimeSpent
        fields = ["activity", "timespent"]


class TimespentListAPIView(generics.ListAPIView):
    serializer_class = TimespentSerializer
    queryset = TimeSpent.objects.all()

class TimespentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TimespentSerializer
    queryset = TimeSpent.objects.all()


# Create your views here.


class RespondentDetailSerializer(serializers.ModelSerializer):

    #time_spent = serializers.PrimaryKeyRelatedField(queryset=TimeSpent.objects.all())

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
