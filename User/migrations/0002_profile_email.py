# Generated by Django 4.2.6 on 2023-12-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='anonymus@gmail.com', max_length=200),
        ),
    ]
