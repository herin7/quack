# Generated by Django 5.1.4 on 2024-12-19 17:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0007_alter_storedcontent_file_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedcontent',
            name='file_content',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file_content'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile-pic'),
        ),
    ]