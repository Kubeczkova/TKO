# Generated by Django 5.1.5 on 2025-02-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tko', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(null=True, upload_to='articles/%Y/%m/%d'),
        ),
    ]
