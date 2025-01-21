

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0028_remove_habit_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='num_of_completed_tasks',
        ),
    ]
