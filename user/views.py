from django.shortcuts import render
from help_or_gtfo_backend.utils import success_response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserView(APIView):
    def get(self, request):
        queryset = CustomUser.objects.all()
        serializer = CustomUserSerializer(queryset, many=True)

        return success_response(serializer.data)
