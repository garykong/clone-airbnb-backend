# Generated by Django 4.1.3 on 2022-11-02 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_house_pets_allowed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='price',
            new_name='price_per_night',
        ),
    ]
