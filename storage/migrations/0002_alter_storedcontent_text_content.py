# Generated by Django 5.1.3 on 2024-12-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedcontent',
            name='text_content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]