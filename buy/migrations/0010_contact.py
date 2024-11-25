# Generated by Django 5.0.7 on 2024-11-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0009_carouselitem_remove_housemodel_secondary_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_icon', models.ImageField(blank=True, null=True, upload_to='contact_icons/')),
                ('email_icon', models.ImageField(blank=True, null=True, upload_to='contact_icons/')),
            ],
        ),
    ]
