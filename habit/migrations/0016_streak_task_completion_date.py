

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0015_alter_habit_num_of_completed_tasks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='streak',
            name='task_completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
