# Generated by Django 4.0.6 on 2022-08-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0010_alter_product_category_alter_product_pvp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de venta'),
        ),
    ]
