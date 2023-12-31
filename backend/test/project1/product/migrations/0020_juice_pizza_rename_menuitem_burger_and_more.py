# Generated by Django 4.2.4 on 2023-08-13 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_delete_burger_delete_juice_delete_pizza_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Pizza', 'Pizza'), ('Burger', 'Burger'), ('Juice', 'Juice')], default='Pizza', max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('characteristic', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('available', models.BooleanField(default=True)),
                ('datime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Pizza', 'Pizza'), ('Burger', 'Burger'), ('Juice', 'Juice')], default='Pizza', max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('characteristic', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('available', models.BooleanField(default=True)),
                ('datime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RenameModel(
            old_name='MenuItem',
            new_name='Burger',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
