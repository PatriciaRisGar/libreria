# Generated by Django 3.2.23 on 2023-12-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_auto_20231212_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/cover/'),
        ),
    ]
