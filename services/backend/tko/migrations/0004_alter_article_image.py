# Generated by Django 5.1.5 on 2025-02-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tko', '0003_rename_first_name_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, default='default.png', upload_to=''),
        ),
    ]
