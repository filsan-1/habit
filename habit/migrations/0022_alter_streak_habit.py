

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0021_delete_habitview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='habit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='streak', to='habit.habit'),
        ),
    ]
