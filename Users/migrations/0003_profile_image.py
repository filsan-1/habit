

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_profile_date_joined_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
