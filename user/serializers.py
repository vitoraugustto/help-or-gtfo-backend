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
