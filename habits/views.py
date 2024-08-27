from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, viewsets

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user_habit = self.request.user
        habit.save()


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(operation_description="Список личных привычек")
)
class HabitOwnListAPIView(generics.ListAPIView):
    """ Список личных привычек авторизованного пользователя. """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        queryset = self.queryset.filter(user_habit=self.request.user)
        return queryset


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(operation_description="Список публичных привычек")
)
class HabitPublicListAPIView(generics.ListAPIView):
    """ Список публичных привычек. """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
