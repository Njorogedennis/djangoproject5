# Generated by Django 4.2.6 on 2023-11-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authyy', '0003_product_image_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(related_name='carts', to='authyy.product')),
            ],
        ),
    ]
