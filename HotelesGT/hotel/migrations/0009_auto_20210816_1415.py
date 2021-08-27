# Generated by Django 3.2.5 on 2021-08-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20210812_1028'),
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
            field=models.CharField(blank=True, choices=[('D', 'Disponible'), ('N', 'No disponible'), ('R', 'Reservado')], default='D', max_length=1, null=True, verbose_name='Estado'),
        ),
    ]