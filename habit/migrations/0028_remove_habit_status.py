

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0027_alter_habit_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='status',
        ),
    ]
