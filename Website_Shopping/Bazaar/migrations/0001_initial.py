# Generated by Django 3.2.9 on 2022-04-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product_pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('free_delivery', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FootWear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product_pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('free_delivery', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prod_id', models.CharField(max_length=10)),
                ('order_date', models.DateTimeField()),
                ('delivery_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SkinCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product_pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('free_delivery', models.BooleanField(default=False)),
            ],
        ),
    ]
