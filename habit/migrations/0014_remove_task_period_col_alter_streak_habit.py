

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0013_alter_task_period_col_alter_task_task_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='period_col',
        ),
        migrations.AlterField(
            model_name='streak',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streak', to='habit.habit'),
        ),
    ]
