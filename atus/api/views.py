
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
from rest_framework import serializers
from rest_framework.generics import ListAPIView
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
    queryset = TimeSpent.objectz.all()


# Create your views here.


class RespondentSerializer(serializers.ModelSerializer):

    #time_spent = serializers.PrimaryKeyRelatedField(queryset=TimeSpent.objects.all())

    class Meta:
        model = Respondent
        fields = ["id", "statistical_weight", "variables", "time_spent"]



class RespondentDetailView(ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
