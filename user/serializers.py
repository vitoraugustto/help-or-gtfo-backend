from django.shortcuts import render
from rest_framework import serializers

from rundown.models import Expedition

from .models import CompletedExpeditions, CustomUser


class TempExpeditionSerializer(serializers.ModelSerializer):
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


class CompletedExpeditionsSerializer(serializers.ModelSerializer):
    expedition = TempExpeditionSerializer()

    class Meta:
        model = CompletedExpeditions
        fields = [
            "expedition",
            "id",
            "cleared_main_sector",
            "cleared_secondary_sector",
            "cleared_overload_sector",
            "prisoner_efficiency",
            "completed_at",
        ]


class CustomUserCompletedExpeditionsSerializer(serializers.ModelSerializer):
    completed_expeditions = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["completed_expeditions"]

    def get_completed_expeditions(self, obj):
        completed_expeditions = CompletedExpeditions.objects.filter(user=obj)

        serializer = CompletedExpeditionsSerializer(completed_expeditions, many=True)

        return serializer.data


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "level",
            "xp",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
        ]


class MinifiedCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "level", "xp"]
