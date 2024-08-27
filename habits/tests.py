from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTest(APITestCase):
    """ Тестирование модели Habit. """
    def setUp(self):
        """ Инициализация теста. """
        self.user_one = User.objects.create(email='test@test.com')
        self.client.force_authenticate(user=self.user_one)
        self.habit_one = Habit.objects.create(
            user_habit=self.user_one,
            place_habit='home test',
            time_habit='09:00',
            action_habit='do test',
            period='daily',
            is_public='True',
        )

    def test_habit_retrieve(self):
        """ Вывод списка тестируемых привычек. """
        url = reverse("habits:habit_detail", args=(self.habit_one.pk,))
        response = self.client.get(url)
        # print(response.json())
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('action_habit'), self.habit_one.action_habit
        )

    def test_habit_create(self):
        """ Создание новой тестируемой привычки. """
        url = reverse("habits:habit_create")
        data = {
            "user_habit": self.user_one.pk,
            "place_habit": "home test 2",
            "time_habit": "10:00",
            "action_habit": "do test 2",
            "period": "daily",
            "is_public": "False",
        }
        response = self.client.post(url, data=data)
        # print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_partial_update(self):
        """ Частичное обновление тестируемой привычки. """
        url = reverse("habits:habit_update", args=(self.habit_one.pk,))
        data = {
            "place_habit": "home test 2 updated",
        }
        response = self.client.patch(url, data=data)
        # print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habit_update(self):
        """ Обновление тестируемой привычки. """
        url = reverse("habits:habit_update", args=(self.habit_one.pk,))
        data = {
            "place_habit": "home test 2 updated",
            "time_habit": "11:00",
            "action_habit": "do test 2 updated",
            "period": "monday",
            "is_public": "False",
        }
        response = self.client.put(url, data=data)
        # print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habit_delete(self):
        """ Удаление тестируемой привычки. """
        url = reverse("habits:habit_destroy", args=(self.habit_one.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_habit_filter_by_user(self):
        """ Фильтрация привычек по создателю. """
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        # print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(len(response.json()['results']), 1)

# class HabitValidateTest(APITestCase):
#     """ Тестирование модели Habit. """
#
#     def setUp(self):
#         """ Инициализация теста. """
#         self.user_two = User.objects.create(email='test2@test.com')
#         self.client.force_authenticate(user=self.user_two)
#
#     def test_duration_habit(self):
#         """ Проверка валидации длительности. Создаем привычку длиной больше 120 секунд. """
#         data = {
#             "user_habit": self.user_two.pk,
#             "place_habit": "home test 2",
#             "time_habit": "10:00",
#             "action_habit": "do test 2",
#             "period": "daily",
#             "is_public": "False",
#             "duration": "01:03",
#         }
#         response = self.client.post('/habit/create/', data=data)
#         self.assertEqual(
#             response.status_code, status.HTTP_400_BAD_REQUEST
#         )
