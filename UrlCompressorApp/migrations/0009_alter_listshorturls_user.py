# Generated by Django 4.2.6 on 2023-12-18 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UrlCompressorApp', '0008_listshorturls_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listshorturls',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
