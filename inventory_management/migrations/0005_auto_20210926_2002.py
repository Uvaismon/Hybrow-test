# Generated by Django 3.2.7 on 2021-09-26 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0004_auto_20210926_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity_in_stock',
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.product')),
            ],
        ),
    ]