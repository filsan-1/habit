

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
