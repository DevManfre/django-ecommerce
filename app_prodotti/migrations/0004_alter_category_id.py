# Generated by Django 4.0.5 on 2022-06-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prodotti', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
