# Generated by Django 4.2.5 on 2023-10-03 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_alter_customuser_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, default='India', max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]