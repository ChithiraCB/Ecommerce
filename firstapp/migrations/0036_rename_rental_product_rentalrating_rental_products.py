# Generated by Django 4.2.5 on 2024-02-28 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0035_rentalrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentalrating',
            old_name='rental_product',
            new_name='rental_products',
        ),
    ]