from django import template
from datetime import date
from ..models import *

register = template.Library()

@register.filter
def dias(fecha_ingreso, fecha_salida):

    fecha = fecha_salida - fecha_ingreso
    return fecha.days +1

@register.filter
def multiplicar(dias, precio):
    return dias * precio

@register.filter
def habitacion(reservacion_id):
    habitacion = Detalle_Reservacion.objects.filter(reservacion_id = reservacion_id)
    numero_habitacion = 0
    for f in habitacion:
        numero_habitacion = f.habitacion_id.numero_habitacion
    return numero_habitacion

@register.filter
def fecha_ingreso(reservacion_id):
    fecha = Detalle_Reservacion.objects.filter(reservacion_id = reservacion_id)
    fecha_ingreso = ''
    for f in fecha:
        fecha_ingreso = f.fecha_ingreso
    return fecha_ingreso

@register.filter
def fecha_salida(reservacion_id):
    fecha = Detalle_Reservacion.objects.filter(reservacion_id = reservacion_id)
    fecha_salida = ''
    for f in fecha:
        fecha_salida = f.fecha_salida
    return fecha_salida