# Generated by Django 4.2.5 on 2024-02-19 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0029_rentalcart_rental_products_rentalcartitem_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentalcart',
            old_name='user',
            new_name='rental_cart_user',
        ),
    ]