from django.contrib import admin
from django.urls import path
import help_or_gtfo_backend.quickstart.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickstart/', views.UserViewSet.as_view({ 'get': 'list' }))
]
