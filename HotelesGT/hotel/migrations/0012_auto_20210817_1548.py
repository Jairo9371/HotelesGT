# Generated by Django 3.2.5 on 2021-08-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_alter_reservacion_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='estado',
            field=models.CharField(blank=True, choices=[('R', 'Reservado'), ('N', 'No disponible'), ('D', 'Disponible')], default='D', max_length=1, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='estado',
            field=models.CharField(blank=True, choices=[('C', 'Cancelada'), ('A', 'Activa'), ('P', 'Pagada')], default='A', max_length=1, null=True, verbose_name='Estado'),
        ),
    ]