from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import status

from help_or_gtfo_backend.utils import error_response, success_response

from .models import CompletedExpeditions, CustomUser
from .serializers import (
    CompletedExpeditionsSerializer,
    CustomUserSerializer,
    MinifiedCustomUserSerializer,
)


class StandardPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5

    def get_paginated_response(self, data):
        return success_response(
            {
                "count": self.page.paginator.count,
                "previous": self.get_previous_link(),
                "next": self.get_next_link(),
                "results": data,
            }
        )


class CustomUserView(viewsets.GenericViewSet):
    pagination_class = StandardPagination

    @action(detail=True, methods=["get"])
    def get_users(self, request):
        order_by = request.GET.get("order_by", "")
        sort_order = request.GET.get("sort_order", "")

        users = CustomUser.objects.filter(is_superuser=False, is_active=True)

        if order_by:
            if sort_order and sort_order != "asc" and sort_order != "desc":
                return error_response(
                    "The 'sort_order' parameter must be specified as 'asc' or 'desc'."
                )

            sort_order = "-" if sort_order == "desc" else ""

            users = users.order_by(sort_order + order_by)

        serializer = MinifiedCustomUserSerializer(users, many=True)

        return success_response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_user_by_id(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            serializer = CustomUserSerializer(user)

            return success_response(serializer.data)

        except CustomUser.DoesNotExist:
            return error_response(
                message="Prisoner not found.", status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return error_response(
                message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # TODO: Add pagination
    @action(detail=True, methods=["get"])
    def get_user_completed_expeditions_by_id(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)

            completed_expeditions = CompletedExpeditions.objects.filter(
                user=user
            ).order_by("expedition")

            page = self.paginate_queryset(completed_expeditions)

            serializer = CompletedExpeditionsSerializer(
                completed_expeditions, many=True
            )

            return self.get_paginated_response(serializer.data)

        except CustomUser.DoesNotExist:
            return error_response(
                message="Prisoner not found.", status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return error_response(
                message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
