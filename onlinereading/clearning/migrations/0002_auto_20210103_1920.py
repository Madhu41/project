# Generated by Django 3.1.3 on 2021-01-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clearning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exfd',
            name='impf',
            field=models.ImageField(default='profile.png', upload_to='Profile/'),
        ),
    ]
