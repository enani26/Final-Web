# Generated by Django 4.2.4 on 2023-08-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_burger_quantity_remove_juice_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juice',
            name='Characteristic',
            field=models.TextField(blank=True, null=True),
        ),
    ]