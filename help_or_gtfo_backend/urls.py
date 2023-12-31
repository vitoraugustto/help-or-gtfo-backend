from django.contrib import admin
from django.urls import include, path

from rundown.views import RundownView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rundowns/", include("rundown.urls")),
    path("api/v1/prisoners/", include("user.urls")),
]
