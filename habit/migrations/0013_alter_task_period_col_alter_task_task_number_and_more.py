
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0012_streak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='period_col',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(max_length=255),
        ),
    ]
