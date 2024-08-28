from datetime import timedelta
from rest_framework.serializers import ValidationError


class RelatedPleasedHabitValidator:
    """В связанные привычки могут попадать только полезные привычки."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            if tmp_val.is_pleasant is not False:
                raise ValidationError("Только полезные привычки могут быть связаны.")


class RelatedRewardHabitValidator:
    """Невозможен одновременный выбор связанной привычки и указания вознаграждения."""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        tmp_val_related_habit = dict(value).get(self.field1)
        tmp_val_reward = dict(value).get(self.field2)
        if tmp_val_related_habit and tmp_val_reward:
            raise ValidationError("Нельзя выбирать связанную привычку и вознаграждение вместе.")


class PleasedRewardHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            check_val = dict(value)
            if check_val.get("reward") is not None or check_val.get("related_habit") is not None:
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class DurationSecondsValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)  # пытаемся получить значение того поля, которое нудно отвалидировать
        if tmp_val is not None and tmp_val > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class FrequencyValidator:
    """Частота выполнения не должна превышать 7 дней."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None and tmp_val > 7:
            raise ValidationError("Время выполнения не может быть более 7 дней.")
