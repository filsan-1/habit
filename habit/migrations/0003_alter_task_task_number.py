

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_number',
            field=models.IntegerField(default=77),
        ),
    ]
