

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0004_task_period_col_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='num_of_tasks',
            field=models.FloatField(),
        ),
    ]
