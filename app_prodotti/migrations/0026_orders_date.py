# Generated by Django 4.0.5 on 2022-06-22 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prodotti', '0025_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 22, 15, 49, 8, 101440)),
        ),
    ]
