from rest_framework import serializers
from rest_framework.serializers import ValidationError
from habits.models import Habit
from habits.validators import (DurationSecondsValidator,
                               PleasedRewardHabitValidator,
                               RelatedPleasedHabitValidator,
                               RelatedRewardHabitValidator, FrequencyValidator)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedPleasedHabitValidator(field='related_habit'),
            RelatedRewardHabitValidator(field1='related_habit', field2='reward'),
            PleasedRewardHabitValidator(field='is_pleasant'),
            DurationSecondsValidator(field='duration'),
            FrequencyValidator(field='frequency')
        ]


