# Generated by Django 5.1.3 on 2024-11-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0006_housemodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Adres'),
        ),
    ]