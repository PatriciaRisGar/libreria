# Generated by Django 3.2.23 on 2023-12-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover'),
        ),
    ]
