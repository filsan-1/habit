

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_alter_task_task_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='period_col',
            field=models.CharField(default='nontype', max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
