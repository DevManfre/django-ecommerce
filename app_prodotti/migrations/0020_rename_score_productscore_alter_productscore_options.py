# Generated by Django 4.0.5 on 2022-06-11 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_utenti', '0005_alter_ecommerceuser_options'),
        ('app_prodotti', '0019_alter_product_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Score',
            new_name='ProductScore',
        ),
        migrations.AlterModelOptions(
            name='productscore',
            options={'verbose_name_plural': 'Recensioni - Prodotti'},
        ),
    ]
