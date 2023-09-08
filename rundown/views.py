from help_or_gtfo_backend.utils import success_response, error_response
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import RundownSerializer, ExpeditionSerializer
from .models import Rundown, Expedition


class RundownView(APIView):
    def get(self, request):
        queryset = Rundown.objects.all()
        serializer = RundownSerializer(queryset, many=True)

        return success_response(serializer.data)

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
                if len(keys_missing) > 1:
                    error_message = "Keys " + ", ".join(keys_missing) + " are missing."
                else:
                    error_message = "Key " + keys_missing[0] + " is missing."
                raise ValueError(error_message)

            rundown = Rundown.objects.create(
                title=title,
                number=number,
                release_date=release_date,
            )

            serializer = RundownSerializer(rundown)

            return Response(serializer.data)

        except ValueError as e:
            return error_response(message=str(e))

        except Exception as e:
            return error_response(
                message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(("GET",))
def get_expedition_by_id(request, rundown_id, expedition_id):
    rundown_id = rundown_id
    expedition_id = expedition_id

    try:
        expedition = Expedition.objects.get(id=expedition_id, rundown__id=rundown_id)
        serializer = ExpeditionSerializer(expedition)

        return success_response(serializer.data)

    except Expedition.DoesNotExist:
        return error_response(
            message="Expedition not found.", status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        return error_response(
            message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
