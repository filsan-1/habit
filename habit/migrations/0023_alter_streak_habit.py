

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0022_alter_streak_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streak', to='habit.habit'),
        ),
    ]
