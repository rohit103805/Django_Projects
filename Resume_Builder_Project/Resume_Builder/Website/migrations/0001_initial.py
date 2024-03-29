# Generated by Django 4.1.7 on 2023-03-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('phone', models.BigIntegerField(primary_key=True, serialize=False)),
                ('about', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('links', models.CharField(max_length=200)),
                ('bachelors', models.CharField(max_length=100)),
                ('bcollege', models.CharField(max_length=100)),
                ('bpercent', models.IntegerField()),
                ('bpass', models.IntegerField()),
                ('stream', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('spercent', models.IntegerField()),
                ('spass', models.IntegerField()),
                ('skill1', models.CharField(max_length=50)),
                ('skill2', models.CharField(max_length=50)),
                ('skill3', models.CharField(max_length=50)),
                ('skill4', models.CharField(max_length=50)),
                ('exp1', models.CharField(max_length=100)),
                ('exp2', models.CharField(max_length=100)),
                ('exp3', models.CharField(max_length=100)),
                ('exp4', models.CharField(max_length=100)),
            ],
        ),
    ]
