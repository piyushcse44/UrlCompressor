# Generated by Django 4.2.6 on 2023-12-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlCompressorApp', '0010_listshorturls_short_url'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='listshorturls',
            index=models.Index(fields=['short_url'], name='UrlCompress_short_u_3ddb0d_idx'),
        ),
    ]
