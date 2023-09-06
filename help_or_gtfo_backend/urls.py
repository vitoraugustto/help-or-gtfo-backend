from django.contrib import admin
from django.urls import path
from rundown.views import RundownView, ExpeditionView
from user.views import CustomUserView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rundowns", RundownView.as_view()),
    path("api/v1/expeditions", ExpeditionView.as_view()),
    path("api/v1/prisoners", CustomUserView.as_view()),
]
