from django.contrib import admin
from django.urls import path
from rundown.views import RundownView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rundowns", RundownView.as_view()),
]
