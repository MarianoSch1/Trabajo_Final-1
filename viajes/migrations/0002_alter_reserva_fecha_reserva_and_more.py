# Generated by Django 4.1.2 on 2022-10-27 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(max_length=200),
        ),
    ]
