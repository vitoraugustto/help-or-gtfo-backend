from .views import RundownView, ExpeditionView
from django.urls import path


urlpatterns = [
    path("", RundownView.as_view()),
    path(
        "<int:rundown_id>/expeditions/<int:expedition_id>",
        ExpeditionView.as_view({"get": "get_expedition_by_id"}),
    ),
    path(
        "<int:rundown_id>/expeditions/<int:expedition_id>/finishers",
        ExpeditionView.as_view({"get": "get_expedition_finishers_by_id"}),
    ),
]
