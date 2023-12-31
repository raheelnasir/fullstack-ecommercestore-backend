# Generated by Django 4.2.1 on 2023-08-28 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApi', '0004_rename_products_orderdetail_product_products_likes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product',
            new_name='order_products',
        ),
        migrations.AlterField(
            model_name='eachorderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='WebApi.products'),
        ),
    ]
