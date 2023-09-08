from django.shortcuts import render
from rest_framework import serializers
from .models import Rundown, Expedition


class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = ["id", "title", "tier", "difficulty", "xp"]


class RundownSerializer(serializers.ModelSerializer):
    expeditions = ExpeditionSerializer(many=True, source="expedition_set")

    class Meta:
        model = Rundown
        fields = ["id", "title", "number", "release_date", "expeditions"]
