

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0026_alter_habit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='status',
            field=models.CharField(default='In progress', max_length=255),
        ),
    ]
