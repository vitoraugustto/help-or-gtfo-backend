from .views import CustomUserView
from django.urls import path

urlpatterns = [
    path("", CustomUserView.as_view({"get": "get_users"})),
    path("<int:user_id>", CustomUserView.as_view({"get": "get_user_by_id"})),
]
