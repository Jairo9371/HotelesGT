# Generated by Django 3.2.6 on 2021-08-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_auto_20210824_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='estado',
            field=models.CharField(blank=True, choices=[('D', 'Disponible'), ('N', 'No disponible'), ('R', 'Reservado')], default='D', max_length=1, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='estado',
            field=models.CharField(blank=True, choices=[('A', 'Activa'), ('P', 'Pagada'), ('C', 'Cancelada')], default='A', max_length=1, null=True, verbose_name='Estado'),
        ),
    ]
