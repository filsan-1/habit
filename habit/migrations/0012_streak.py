

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0011_task_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Streak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_completed_tasks', models.IntegerField(default=0)),
                ('num_of_failed_tasks', models.IntegerField(default=0)),
                ('longest_streak', models.IntegerField(default=0)),
                ('current_streak', models.IntegerField(default=0)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habit.habit')),
            ],
        ),
    ]
