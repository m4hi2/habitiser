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
        return f"{self.name}"


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
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    goal = models.CharField(max_length=255, blank=True, null=True)  # Example: "Run 2KM"

    class Meta:
        unique_together = ("habit", "day")  # Prevent duplicate schedules

    def __str__(self):
        return f"{self.habit.name} on {self.day}"


class HabitTracker(models.Model):
    """Tracks habit completion per day."""
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="trackers")
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("habit", "date")  # Ensures only one entry per habit per day

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.completed else 'Pending'}"