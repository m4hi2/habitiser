from django.db import models
from django.utils import timezone

from users.models import User


# Create your models here.
class Habit(models.Model):
    """Stores habits that a user wants to track."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.email})"


class HabitSchedule(models.Model):
    """Defines the schedule for each habit."""
    DAYS_OF_WEEK = [
        ("Sunday", "Sunday"),
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    ]

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="schedules")
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    goal = models.CharField(max_length=255, blank=True, null=True)  # Example: "Run 2KM"

    class Meta:
        unique_together = ("habit", "day_of_week")  # Prevent duplicate schedules

    def __str__(self):
        return f"{self.habit.name} on {self.day_of_week}"


class HabitProgress(models.Model):
    """Tracks when a user completes a habit."""
    habit_schedule = models.ForeignKey(HabitSchedule, on_delete=models.CASCADE, related_name="progress")
    date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("habit_schedule", "date")  # Prevent duplicate entries for the same day

    def __str__(self):
        return f"{self.habit_schedule.habit.name} on {self.date} - {'Completed' if self.completed else 'Pending'}"