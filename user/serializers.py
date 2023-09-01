from django.shortcuts import render
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "is_active", "is_staff", "is_superuser", "date_joined"]
