# Generated by Django 4.2.5 on 2024-03-15 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0039_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_reason', models.CharField(choices=[('Damaged', 'Damaged'), ('Wrong item received', 'Wrong item received'), ('Not as described', 'Not as described'), ('Changed mind', 'Changed mind'), ('Other', 'Other')], max_length=50)),
                ('return_comments', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.order')),
            ],
        ),
    ]