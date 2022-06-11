# Generated by Django 4.0.5 on 2022-06-11 00:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_utenti', '0005_alter_ecommerceuser_options'),
        ('app_prodotti', '0013_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_prodotti.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_utenti.ecommerceuser')),
            ],
            options={
                'verbose_name_plural': 'Recensioni',
            },
        ),
    ]
