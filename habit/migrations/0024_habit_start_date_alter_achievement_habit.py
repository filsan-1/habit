

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0023_alter_streak_habit'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievement', to='habit.habit'),
        ),
    ]
