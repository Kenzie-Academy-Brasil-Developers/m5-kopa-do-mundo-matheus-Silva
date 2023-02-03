from django.contrib import admin
from django.urls import path 

from teams.views import TeamView ,TeamDetailsView

urlpatterns = [
    path("teams/" , TeamView.as_view()),
    path("teams/<int:team_id>/", TeamDetailsView.as_view())
]
