# Generated by Django 4.2.6 on 2023-12-18 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UrlCompressorApp', '0011_listshorturls_urlcompress_short_u_3ddb0d_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='listshorturls',
            name='UrlCompress_unique__a8b1bc_idx',
        ),
        migrations.RemoveField(
            model_name='listshorturls',
            name='unique_key',
        ),
    ]