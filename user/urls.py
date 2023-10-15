from django.urls import path

from .views import CustomUserView

urlpatterns = [
    path("", CustomUserView.as_view({"get": "get_users"})),
    path("<int:user_id>", CustomUserView.as_view({"get": "get_user_by_id"})),
    path(
        "<int:user_id>/completed-expeditions",
        CustomUserView.as_view({"get": "get_user_completed_expeditions_by_id"}),
    ),
]
