# Generated by Django 4.2.5 on 2023-11-05 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_category1_subcategory1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('stock', models.PositiveIntegerField(default=1, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sale_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('status', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], default='In Stock', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.category1')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.subcategory1')),
            ],
        ),
    ]
