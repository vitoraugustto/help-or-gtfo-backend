from django.shortcuts import render
from rest_framework import serializers

from user.models import CustomUser
from user.serializers import MinifiedCustomUserSerializer

from .models import Expedition, Rundown


class MinifiedExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = ["id", "display_name"]


class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = [
            "id",
            "display_name",
            "title",
            "main_sector",
            "secondary_sector",
            "overload_sector",
            "tier",
            "difficulty",
            "xp",
        ]


class ExpeditionFinishersSerializer(serializers.ModelSerializer):
    finishers = serializers.SerializerMethodField()

    class Meta:
        model = Expedition
        fields = [
            "finishers",
        ]

    def get_finishers(self, obj):
        finishers = CustomUser.objects.filter(completed_expeditions=obj)
        unique_finishers = set(finishers)

        serializer = MinifiedCustomUserSerializer(unique_finishers, many=True)

        return serializer.data


class RundownSerializer(serializers.ModelSerializer):
    expeditions = MinifiedExpeditionSerializer(many=True, source="expedition_set")

    class Meta:
        model = Rundown
        fields = ["id", "title", "number", "release_date", "expeditions"]
