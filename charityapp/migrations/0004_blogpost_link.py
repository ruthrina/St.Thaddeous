# Generated by Django 5.1.6 on 2025-02-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0003_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='link',
            field=models.URLField(default='https://example.com'),
        ),
    ]
