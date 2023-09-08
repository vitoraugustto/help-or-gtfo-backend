from .views import RundownView, get_expedition_by_id
from django.urls import path


urlpatterns = [
    path("", RundownView.as_view()),
    path("<int:rundown_id>/expeditions/<int:expedition_id>", get_expedition_by_id),
]
