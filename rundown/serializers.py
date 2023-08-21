from django.shortcuts import render
from rest_framework import serializers
from .models import Rundown, Expedition


class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = ["id", "title", "tier", "difficulty", "xp", "rundown"]


class RundownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rundown
        fields = ["id", "title", "number", "release_date"]
