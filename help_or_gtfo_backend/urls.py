from django.contrib import admin
from django.urls import path
from rundown.views import RundownView, ExpeditionView, get_expedition_by_id
from user.views import CustomUserView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rundowns", RundownView.as_view()),
    path(
        "api/v1/rundowns/<int:rundown_id>/expeditions/<int:expedition_id>",
        get_expedition_by_id,
    ),
    path("api/v1/prisoners", CustomUserView.as_view()),
]
