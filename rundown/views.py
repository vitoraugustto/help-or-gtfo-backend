from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import RundownSerializer
from .models import Rundown


class RundownView(APIView):
    def get(self, request):
        queryset = Rundown.objects.all()
        serializer = RundownSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        try:
            title = request.data.get("title")
            number = request.data.get("number")
            release_date = request.data.get("release_date")

            keys_missing = []

            if title is None:
                keys_missing.append("'title'")

            if number is None:
                keys_missing.append("'number'")

            if release_date is None:
                keys_missing.append("'release_date'")

            if keys_missing:
                error_message = (
                    ("Keys " if len(keys_missing) > 1 else "Key ")
                    + ", ".join(keys_missing)
                    + " are missing."
                )
                raise ValueError(error_message)

            rundown = Rundown.objects.create(
                title=title,
                number=number,
                release_date=release_date,
            )

            serializer = RundownSerializer(rundown)

            return Response(serializer.data)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
