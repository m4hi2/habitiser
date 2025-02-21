from django import forms
from .models import Habit, HabitSchedule, HabitProgress


class HabitForm(forms.ModelForm):
    """Form for creating and updating habits."""
    class Meta:
        model = Habit
        fields = ["name", "description"]


class HabitScheduleForm(forms.ModelForm):
    """Form for assigning days to a habit."""
    class Meta:
        model = HabitSchedule
        fields = ["habit", "day_of_week", "goal"]


class HabitProgressForm(forms.ModelForm):
    """Form for marking habit progress."""
    class Meta:
        model = HabitProgress
        fields = ["habit_schedule", "date", "completed"]
