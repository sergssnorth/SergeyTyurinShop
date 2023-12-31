# Generated by Django 5.0 on 2023-12-11 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_availableproductsizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AvailableProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_product_size', to='product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_product_size', to='product.productsize')),
            ],
            options={
                'ordering': ('product',),
            },
        ),
        migrations.DeleteModel(
            name='AvailableProductSizes',
        ),
    ]
