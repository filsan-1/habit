

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0010_remove_habit_number_of_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
