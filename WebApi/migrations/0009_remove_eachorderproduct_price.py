# Generated by Django 4.2.1 on 2023-08-28 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApi', '0008_remove_products_likes_remove_products_reviews_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eachorderproduct',
            name='price',
        ),
    ]