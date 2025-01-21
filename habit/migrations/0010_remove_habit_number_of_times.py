

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0009_habit_num_of_completed_tasks_task_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='number_of_times',
        ),
    ]
