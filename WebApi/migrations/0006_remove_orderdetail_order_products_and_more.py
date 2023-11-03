# Generated by Django 4.2.1 on 2023-08-28 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApi', '0005_rename_product_orderdetail_order_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='order_products',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='comments',
        ),
        migrations.AlterField(
            model_name='eachorderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='WebApi.products'),
        ),
    ]