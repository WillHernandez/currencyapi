# Generated by Django 4.0.3 on 2022-03-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencyapi', '0007_alter_currency_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rates',
            field=models.TextField(verbose_name='Rates'),
        ),
    ]
