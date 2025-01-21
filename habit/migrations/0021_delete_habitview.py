

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0020_habitview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HabitView',
        ),
    ]
