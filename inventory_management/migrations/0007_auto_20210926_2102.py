# Generated by Django 3.2.7 on 2021-09-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0006_alter_stock_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmovement',
            name='id',
        ),
        migrations.AlterField(
            model_name='productmovement',
            name='movement_id',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
    ]
