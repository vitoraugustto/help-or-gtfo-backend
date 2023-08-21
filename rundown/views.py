from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RundownSerializer
from .models import Rundown


class RundownView(APIView):
    def get(self, request):
        queryset = Rundown.objects.all()
        serializer = RundownSerializer(queryset, many=True)

        return Response(serializer.data)
