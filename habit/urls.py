from django.urls import path
from .views import habit_list, add_habit, add_schedule, mark_complete

urlpatterns = [
    path("", habit_list, name="habit_list"),
    path("add-habit/", add_habit, name="add_habit"),
    path("add-schedule/", add_schedule, name="add_schedule"),
    path("mark-complete/<int:tracker_id>/", mark_complete, name="mark_complete"),
]
