from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "user_habit",
        "place_habit",
        "time_habit",
        "action_habit",
        "frequency",
    )
