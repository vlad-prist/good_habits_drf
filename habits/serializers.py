from rest_framework import serializers

from habits.models import Habit
from habits.validators import (DurationSecondsValidator, FrequencyValidator,
                               PleasedRewardHabitValidator,
                               RelatedPleasedHabitValidator,
                               RelatedRewardHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RelatedPleasedHabitValidator(field="related_habit"),
            RelatedRewardHabitValidator(field1="related_habit", field2="reward"),
            PleasedRewardHabitValidator(field="is_pleasant"),
            DurationSecondsValidator(field="duration"),
            FrequencyValidator(field="frequency"),
        ]
