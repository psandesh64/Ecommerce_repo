# Generated by Django 4.2.1 on 2023-06-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cart_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]