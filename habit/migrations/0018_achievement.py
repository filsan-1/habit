

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0017_remove_streak_task_completion_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streak_length', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='habit.habit')),
            ],
        ),
    ]
