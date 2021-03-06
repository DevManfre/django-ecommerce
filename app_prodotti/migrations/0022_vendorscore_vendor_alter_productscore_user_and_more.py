# Generated by Django 4.0.5 on 2022-06-11 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_utenti', '0005_alter_ecommerceuser_options'),
        ('app_prodotti', '0021_vendorscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorscore',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Address1', to='app_utenti.ecommerceuser'),
        ),
        migrations.AlterField(
            model_name='productscore',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_utenti.ecommerceuser'),
        ),
        migrations.AlterField(
            model_name='vendorscore',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_utenti.ecommerceuser'),
        ),
    ]
