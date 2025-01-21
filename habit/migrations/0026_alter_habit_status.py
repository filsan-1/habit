

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0025_habit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]
