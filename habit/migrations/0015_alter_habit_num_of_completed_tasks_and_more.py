

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0014_remove_task_period_col_alter_streak_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='num_of_completed_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='habit',
            name='num_of_tasks',
            field=models.IntegerField(),
        ),
    ]
