# Generated by Django 4.2.4 on 2023-08-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bid_user_product_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
