# Generated by Django 5.2.1 on 2025-05-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='carros/'),
        ),
    ]
