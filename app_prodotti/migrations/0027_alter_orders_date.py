# Generated by Django 4.0.5 on 2022-06-22 13:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_prodotti', '0026_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 22, 13, 50, 6, 523322, tzinfo=utc)),
        ),
    ]
