from django.shortcuts import render
from help_or_gtfo_backend.utils import success_response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MinifiedCustomUserSerializer
from .models import CustomUser


class CustomUserView(APIView):
    def get(self, request):
        order_by = request.GET.get("order_by", "")
        sort_order = request.GET.get("sort_order", "")

        users = CustomUser.objects.filter(is_superuser=False, is_active=True)

        if order_by:
            sort_order = "-" if sort_order == "desc" else ""

            users = users.order_by(sort_order + order_by)

        serializer = MinifiedCustomUserSerializer(users, many=True)

        return success_response(serializer.data)
