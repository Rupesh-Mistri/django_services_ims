# Generated by Django 5.1.3 on 2024-11-19 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.IntegerField()),
                ('invoice_date', models.DateField()),
                ('supplier_id', models.BigIntegerField()),
                ('status', models.IntegerField(default=1)),
                ('purchase_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'purchase_master',
            },
        ),
        migrations.CreateModel(
            name='Temp_purchase_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('stampdatetime', models.DateField(auto_now=True)),
                ('item_id', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'temp_purchase_details',
            },
        ),
        migrations.CreateModel(
            name='Purchase_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('stampdatetime', models.DateField(auto_now=True)),
                ('item', models.BigIntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase_master.purchase_master')),
            ],
            options={
                'db_table': 'purchase_details',
            },
        ),
    ]
