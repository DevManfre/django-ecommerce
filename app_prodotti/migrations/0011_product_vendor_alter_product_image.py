# Generated by Django 4.0.5 on 2022-06-10 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_utenti', '0005_alter_ecommerceuser_options'),
        ('app_prodotti', '0010_alter_product_image_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='app_utenti.ecommerceuser'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
