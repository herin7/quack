# Generated by Django 5.1.4 on 2024-12-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='No bio provided', null=True),
        ),
    ]
