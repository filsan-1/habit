

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0005_alter_habit_num_of_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
