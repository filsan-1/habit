

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0018_achievement'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='TaskTracker',
        ),
        migrations.AlterField(
            model_name='achievement',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habit.habit'),
        ),
    ]
