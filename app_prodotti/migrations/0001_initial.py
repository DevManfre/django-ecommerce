# Generated by Django 4.0.5 on 2022-06-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Prodotti',
            },
        ),
    ]