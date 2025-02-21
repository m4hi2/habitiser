from django.urls import path
from . import views

urlpatterns = [
    path("", views.habit_list, name="habit_list"),
    path("add/", views.add_habit, name="add_habit"),
    path("add-schedule/", views.add_schedule, name="add_schedule"),
    path("progress/<int:habit_schedule_id>/", views.mark_progress, name="mark_progress"),
]
