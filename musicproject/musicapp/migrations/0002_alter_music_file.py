# Generated by Django 4.2.1 on 2023-05-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(upload_to='gallery'),
        ),
    ]
