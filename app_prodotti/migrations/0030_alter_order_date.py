# Generated by Django 4.0.5 on 2022-06-30 10:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_prodotti', '0029_alter_order_date_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 30, 10, 3, 46, 896847, tzinfo=utc)),
        ),
    ]
