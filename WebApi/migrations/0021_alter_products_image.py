# Generated by Django 4.2.6 on 2023-11-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApi', '0020_alter_products_image_alter_products_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='path/to/default_image.jpg', upload_to='product_images/'),
        ),
    ]
