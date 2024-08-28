from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    user_habit = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="создатель привычки",
    )
    place_habit = models.CharField(
        max_length=200, verbose_name="место, в котором необходимо выполнять привычку"
    )
    time_habit = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="время, когда необходимо выполнять привычку",
        help_text="HH:MM",
    )
    action_habit = models.CharField(
        max_length=350, verbose_name="действие, которое представляет собой привычка"
    )
    is_pleasant = models.BooleanField(
        default=False, verbose_name="признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    reward = models.CharField(max_length=300, verbose_name="вознаграждение", **NULLABLE)
    duration = models.DurationField(verbose_name="Время на выполнение", **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name="признак публичности")
    frequency = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность выполнения привычки (дней)",
        help_text="Привычку выполнять каждые * дней",
    )

    def __str__(self):
        return f"{self.user_habit.email}: {self.action_habit}, {self.time_habit}, {self.place_habit}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
