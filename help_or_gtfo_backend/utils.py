from rest_framework.response import Response
from rest_framework.views import status


def success_response(payload, message="", status=status.HTTP_200_OK):
    return Response(
        {"status": "success", "message": message, "payload": payload}, status=status
    )


def error_response(message="", status=status.HTTP_400_BAD_REQUEST):
    return Response(
        {"status": "error", "message": message, "payload": None}, status=status
    )
