from django.shortcuts import render
from rest_framework import serializers
from .models import Rundown, Expedition
from user.models import CustomUser
from user.serializers import MinifiedCustomUserSerializer


class MinifiedExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = ["id", "display_name"]


class ExpeditionSerializer(serializers.ModelSerializer):
    finishers = serializers.SerializerMethodField()

    class Meta:
        model = Expedition
        fields = [
            "id",
            "display_name",
            "title",
            "tier",
            "difficulty",
            "xp",
            "finishers",
        ]

    def get_finishers(self, obj):
        finishers = CustomUser.objects.filter(completed_expeditions=obj)
        serializer = MinifiedCustomUserSerializer(finishers, many=True)

        return serializer.data


class RundownSerializer(serializers.ModelSerializer):
    expeditions = MinifiedExpeditionSerializer(many=True, source="expedition_set")

    class Meta:
        model = Rundown
        fields = ["id", "title", "number", "release_date", "expeditions"]
