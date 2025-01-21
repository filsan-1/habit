

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0016_streak_task_completion_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streak',
            name='task_completion_date',
        ),
        migrations.AddField(
            model_name='task',
            name='task_completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
