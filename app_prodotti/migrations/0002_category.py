# Generated by Django 4.0.5 on 2022-06-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prodotti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categorie',
            },
        ),
    ]
