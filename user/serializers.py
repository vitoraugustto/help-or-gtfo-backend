from django.shortcuts import render
from rest_framework import serializers
from .models import CustomUser


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
