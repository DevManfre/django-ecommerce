# Generated by Django 4.0.5 on 2022-06-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prodotti', '0009_alter_brand_name_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='C:\\Users\\manfr\\Documents\\DOCUMENTI\\Progetti\\django-ecommerce\\static\\images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
