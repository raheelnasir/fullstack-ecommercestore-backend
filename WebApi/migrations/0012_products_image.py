# Generated by Django 4.2.1 on 2023-08-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApi', '0011_remove_orderdetail_order_remove_orderdetail_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.CharField(default='https://cdn.leonardo.ai/users/9c5c81ee-0af6-45d2-a406-940450d62697/generations/fa323540-75a5-4e72-b957-2ec6a1e5bdf1/DreamShaper_v7_watch_modern_wallpaper_product_full_screened_wr_0.jpg', max_length=999999),
        ),
    ]
