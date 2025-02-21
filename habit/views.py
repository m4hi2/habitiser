from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import HabitForm, HabitScheduleForm
from .models import Habit, HabitSchedule, HabitProgress


@login_required
def habit_list(request):
    """Display user's habits and their schedules."""
    habits = Habit.objects.filter(user=request.user)
    return render(request, "habits/habit_list.html", {"habits": habits})


@login_required
def add_habit(request):
    """Add a new habit."""
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habit_list")
    else:
        form = HabitForm()
    return render(request, "habits/add_habit.html", {"form": form})


@login_required
def add_schedule(request):
    """Assign a day to a habit."""
    if request.method == "POST":
        form = HabitScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("habit_list")
    else:
        form = HabitScheduleForm()
    return render(request, "habits/add_schedule.html", {"form": form})


@login_required
def mark_progress(request, habit_schedule_id):
    """Mark a habit as completed for today."""
    habit_schedule = get_object_or_404(HabitSchedule, id=habit_schedule_id)

    progress, created = HabitProgress.objects.get_or_create(
        habit_schedule=habit_schedule, date=timezone.now()
    )

    progress.completed = not progress.completed
    progress.save()

    return redirect("habit_list")
