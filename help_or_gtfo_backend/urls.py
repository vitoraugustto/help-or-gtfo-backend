from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import help_or_gtfo_backend.quickstart.views as views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
