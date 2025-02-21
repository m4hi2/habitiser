from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Habit, HabitSchedule, HabitTracker
from .forms import HabitForm, HabitScheduleForm


@login_required
def habit_list(request):
    """Show list of habits scheduled for today."""
    today = now().strftime("%A")  # Get today's weekday name
    habits_today = HabitSchedule.objects.filter(day=today, habit__user=request.user)

    for habit_schedule in habits_today:
        HabitTracker.objects.get_or_create(habit=habit_schedule.habit, date=now().date())

    habit_trackers = HabitTracker.objects.filter(date=now().date(), habit__user=request.user)

    return render(request, "habits/habit_list.html", {"habit_trackers": habit_trackers})


@login_required
def add_habit(request):
    """Create a new habit."""
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
    """Add schedule days to a habit."""
    if request.method == "POST":
        form = HabitScheduleForm(request.POST, user=request.user)
        if form.is_valid():
            for day in form.cleaned_data["days"]:
                HabitSchedule.objects.get_or_create(habit=form.cleaned_data["habit"], day=day)
            return redirect("habit_list")
    else:
        form = HabitScheduleForm(user=request.user)
    return render(request, "habits/add_schedule.html", {"form": form, "habits":
        Habit.objects.filter(
        user=request.user)})


@login_required
def mark_complete(request, tracker_id):
    """Mark a habit as completed for today."""
    tracker = HabitTracker.objects.get(id=tracker_id, habit__user=request.user)
    tracker.completed = True
    tracker.save()
    return redirect("habit_list")
