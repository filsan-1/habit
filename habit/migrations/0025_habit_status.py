

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0024_habit_start_date_alter_achievement_habit'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='status',
            field=models.CharField(default='In progress', max_length=255),
        ),
    ]
