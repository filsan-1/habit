

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habit', '0007_alter_habit_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='goal',
            field=models.IntegerField(default=90),
        ),
        migrations.AlterField(
            model_name='habit',
            name='notes',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
