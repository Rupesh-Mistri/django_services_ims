# Generated by Django 5.1.3 on 2024-11-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField()),
                ('status', models.IntegerField(default=1)),
                ('timestamp', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'supplier_master',
            },
        ),
    ]
