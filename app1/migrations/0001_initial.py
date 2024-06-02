# Generated by Django 5.0.6 on 2024-05-31 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=50)),
                ('proveedor', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('precio_unidad', models.FloatField()),
                ('precio_ganancias', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('precio', models.FloatField()),
                ('descuento', models.FloatField()),
                ('total', models.FloatField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.producto')),
            ],
        ),
    ]
