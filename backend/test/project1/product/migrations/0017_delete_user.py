# Generated by Django 4.2.4 on 2023-08-11 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_remove_user_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
