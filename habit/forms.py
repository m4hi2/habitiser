from django import forms
from .models import Habit, HabitSchedule


class HabitForm(forms.ModelForm):
    """Form for creating and updating habits."""
    class Meta:
        model = Habit
        fields = ["name", "description"]


class HabitScheduleForm(forms.ModelForm):
    """Form for assigning days to a habit."""
    habit = forms.ModelChoiceField(queryset=Habit.objects.none(), label="Select Habit")  # Default to empty queryset

    days = forms.MultipleChoiceField(
        choices=HabitSchedule.DAYS_OF_WEEK,
        widget=forms.CheckboxSelectMultiple,
        label="Select Days",
    )

    class Meta:
        model = HabitSchedule
        fields = ["habit", "days", "goal"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["habit"].queryset = Habit.objects.filter(user=user)