# Generated by Django 4.2.4 on 2023-08-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_burger_characteristic'),
    ]

    operations = [
        migrations.AddField(
            model_name='juice',
            name='datime',
            field=models.DateTimeField(null=True),
        ),
    ]