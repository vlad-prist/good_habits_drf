from datetime import timedelta

from rest_framework.serializers import ValidationError


class RelatedPleasedHabitValidator:
    """ В связанные привычки могут попадать только полезные привычки. """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            if tmp_val.is_pleasant is not False:
                raise ValidationError("В связанные привычки могут попадать только полезные привычки.")


class RelatedRewardHabitValidator:
    """ Невозможен одновременный выбор связанной привычки и указания вознаграждения. """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        tmp_val_related_habit = dict(value).get(self.field1)
        tmp_val_reward = dict(value).get(self.field2)
        if tmp_val_related_habit and tmp_val_reward:
            raise ValidationError("Невозможен одновременный выбор связанной привычки и указания вознаграждения.")


class PleasedRewardHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            check_val = dict(value)
            if check_val.get('reward') is not None or check_val.get('related_habit') is not None:
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class DurationSecondsValidator:
    """ Время выполнения должно быть не больше 120 секунд. """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field) # пытаемся получить значение того поля, которое нудно отвалидировать
        if tmp_val is not None and tmp_val > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class DurationDaysValidator:
    """-"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)

        if 7 < tmp_val or tmp_val < 1:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
