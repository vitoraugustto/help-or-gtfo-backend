from django.contrib import admin
from django.urls import path, include
from rundown.views import RundownView, get_expedition_by_id
from user.views import CustomUserView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/prisoners", CustomUserView.as_view()),
    path("api/v1/rundowns/", include("rundown.urls")),
]
