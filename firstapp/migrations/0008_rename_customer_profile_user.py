# Generated by Django 4.2.5 on 2023-11-07 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='customer',
            new_name='user',
        ),
    ]
