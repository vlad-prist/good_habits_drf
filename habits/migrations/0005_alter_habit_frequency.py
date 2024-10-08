# Generated by Django 5.1 on 2024-08-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_remove_habit_when_do_habit_habit_frequency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="frequency",
            field=models.SmallIntegerField(
                default=1,
                help_text="Привычку выполнять каждые * дней",
                verbose_name="Периодичность выполнения привычки (дней)",
            ),
        ),
    ]
