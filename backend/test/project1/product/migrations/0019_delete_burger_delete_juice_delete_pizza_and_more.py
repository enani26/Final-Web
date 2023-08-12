# Generated by Django 4.2.4 on 2023-08-12 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_cartitem_menuitem_order_cartitem_menu_item_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Burger',
        ),
        migrations.DeleteModel(
            name='juice',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Burger', 'Burger'), ('Juice', 'Juice')], default='Pizza', max_length=50),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='characteristic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='datime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
