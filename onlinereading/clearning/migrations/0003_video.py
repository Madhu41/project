# Generated by Django 3.1.3 on 2021-01-06 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clearning', '0002_auto_20210103_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video/%y')),
            ],
        ),
    ]
