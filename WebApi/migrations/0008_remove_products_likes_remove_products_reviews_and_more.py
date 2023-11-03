# Generated by Django 4.2.1 on 2023-08-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApi', '0007_rename_order_eachorderproduct_orderid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='products',
            name='reviews',
        ),
        migrations.AlterField(
            model_name='eachorderproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]