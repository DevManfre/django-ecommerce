# Generated by Django 4.0.5 on 2022-06-07 16:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_utenti', '0002_remove_costumer_birthdate_remove_vendor_birthdate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendor',
            new_name='EcommerceUser',
        ),
        migrations.AlterModelOptions(
            name='ecommerceuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.DeleteModel(
            name='Costumer',
        ),
    ]