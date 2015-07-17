
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
from .models import TimeSpent
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