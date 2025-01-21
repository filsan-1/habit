

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0006_alter_habit_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
