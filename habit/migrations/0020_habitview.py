

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0019_rename_task_tasktracker_alter_achievement_habit'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitView',
            fields=[
                ('tasktracker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='habit.tasktracker')),
            ],
            bases=('habit.tasktracker',),
        ),
    ]
