from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.db import transaction
from datetime import date
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = '/admin')

def index(request):
    titulo = 'BIENVENIDOS AL INICIO'
    template = loader.get_template('index.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url = '/admin')

def hoteles(request):
    titulo = 'HOTELES'
    template = loader.get_template('hoteles.html')
    lista_hoteles = Hotel.objects.all().order_by('-nombre')
    lista_ciudades = Ciudad.objects.all()


    if request.method == "GET":
       ciudad = request.GET.get("ciudad", None)
       if ciudad:
           lista_hoteles = Hotel.objects.filter(ciudad_id = ciudad)

    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
        'lista_hoteles' : lista_hoteles,
        'lista_ciudades' : lista_ciudades,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url = '/admin')

def habitaciones(request):
    titulo = 'HABITACIONES'
    template = loader.get_template('habitaciones.html')
    lista_habitacion = ''
    nombre_hotel = ''
    lista_hoteles = Hotel.objects.all()
    lista_clientes = Cliente.objects.all()


    if request.method == "GET":
        print("METODO GET")

        hotel_seleccionado = request.GET.get("hotel_seleccionado", None)
        if hotel_seleccionado:
            try:
                lista_habitacion = Habitacion.objects.filter(hotel_id = hotel_seleccionado)
                nombre_hotel = Hotel.objects.get(pk = hotel_seleccionado)
            except:
                lista_habitacion = ''


    
    if request.method == "POST":
        print("METODO POST")

        fecha_ingreso = request.POST.get("fecha_ingreso",None)
        fecha_salida = request.POST.get("fecha_salida",None)
        cliente = request.POST.get("cliente",None)
        description = request.POST.get("description",None)
        nombre_reservacion = request.POST.get("nombre_reservacion",None)
        habitacion = request.POST.get("habitacion",None)
        añadir_reservacion = request.POST.get("añadir_reservacion", None)
        hotel = request.POST.get("hotel", None)

        if añadir_reservacion:
            with transaction.atomic():
                fecha_de_hoy = date.today()
                nueva_reservacion = Reservacion.objects.create(
                    fecha = fecha_de_hoy,
                    cliente_id = Cliente.objects.get(pk = cliente),
                    hotel_id = Hotel.objects.get(pk = hotel),
                    description = description,
                    usuario_id = request.user,
                )
                detalle_reservacion = Detalle_Reservacion.objects.create(
                    reservacion_id = Reservacion.objects.all().last(),
                    habitacion_id = Habitacion.objects.get(pk = habitacion),
                    fecha_ingreso= fecha_ingreso,
                    fecha_salida= fecha_salida,
                    nombre_reservacion = nombre_reservacion,
                )
                cambiar_estado_habitacion = Habitacion.objects.get(pk = habitacion)
                cambiar_estado_habitacion.estado = 'R'
                cambiar_estado_habitacion.save()
                messages.info(request,"La reservacion ha sido ingresada")


    
    context = {
        'titulo' : titulo,
        'lista_habitacion' : lista_habitacion,
        'lista_hoteles' : lista_hoteles,
        'nombre_hotel' : nombre_hotel,
        'lista_clientes' : lista_clientes,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url = '/admin')

def clientes(request):
    titulo = 'CLIENTES'
    template = loader.get_template('clientes.html')
    lista_clientes = Cliente.objects.all().order_by('-identificador')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        nombre = request.POST.get("nombre", None)
        apellido = request.POST.get("apellido", None)
        nit = request.POST.get("nit", None)
        telefono = request.POST.get("telefono", None)
        direccion = request.POST.get("direccion", None)
        correo = request.POST.get("correo", None)
        añadir_cliente = request.POST.get("añadir_cliente", None)
        eliminar_cliente = request.POST.get("eliminar_cliente", None)
        modificar_cliente = request.POST.get("modificar_cliente", None)
        identificador = request.POST.get("identificador", None)

        if modificar_cliente:
            datos_cliente = Cliente.objects.get(identificador = identificador)
            with transaction.atomic():
                datos_cliente.nombre = nombre
                datos_cliente.apellido = apellido
                datos_cliente.nit = nit
                datos_cliente.telefono = telefono
                datos_cliente.direccion = direccion
                datos_cliente.correo_electronico = correo
                datos_cliente.save()

        if eliminar_cliente:
            with transaction.atomic():
                Cliente.objects.filter(identificador = eliminar_cliente).delete()

        if añadir_cliente:
            with transaction.atomic():
                añadir_cliente = Cliente.objects.create(
                    nombre = nombre,
                    apellido = apellido,
                    nit = nit,
                    telefono = telefono,
                    direccion = direccion,
                    correo_electronico = correo,
                )


    context = {
        'titulo' : titulo,
        'lista_clientes' : lista_clientes,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url = '/admin')

def reservaciones(request):
    titulo = 'RESERVACIONES'
    template = loader.get_template('reservaciones.html')
    lista_reservaciones = Detalle_Reservacion.objects.select_related('reservacion_id').order_by('-identificador')


    if request.method == "GET":
        print("METODO GET")

        reservacion_id = request.GET.get("reservacion_id", None)
        
        if reservacion_id:
            reservacion = Reservacion.objects.get(pk = reservacion_id)
            reservacion.estado = 'C'
            reservacion.save()
        
    if request.method == "POST":
        print("METODO POST")
        identificador = request.POST.get("identificador", None)
        numero_reservacion = request.POST.get("numero_reservacion", None)
        fecha_ingreso = request.POST.get("fecha_ingreso", None)
        fecha_salida = request.POST.get("fecha_salida", None)
        nombre_reservacion = request.POST.get("nombre_reservacion", None)
        numero_habitacion = request.POST.get("numero_habitacion", None)
        modificar_reservacion = request.POST.get("modificar_reservacion", None)
        total = request.POST.get("total", None)
        description = request.POST.get("description", None)
        facturar = request.POST.get("facturar", None)

        if facturar:
            fecha_de_hoy = date.today()
            with transaction.atomic():

                reservacion = Reservacion.objects.get(pk = numero_reservacion)
                Factura.objects.create(
                    fecha = fecha_de_hoy,
                    description = description,
                    total = Decimal(total.replace(',', '.')),
                    reservacion_id = reservacion,
                )
                reservacion.estado = 'P'
                reservacion.save()
                messages.error(request, "Factura Generada Exitosamente!!!")

        if modificar_reservacion:
            with transaction.atomic():
                objReservacion = Detalle_Reservacion.objects.get(identificador = identificador)
                objReservacion.fecha_ingreso = fecha_ingreso
                objReservacion.fecha_salida = fecha_salida
                objReservacion.nombre_reservacion = nombre_reservacion
                objReservacion.numero_habitacion = numero_habitacion
                objReservacion.save()
                messages.success(request,"Se ha Modificado Correctamente")

 
    context = {
        'titulo' : titulo,
        'lista_reservaciones' : lista_reservaciones,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url = '/admin')

def facturas(request):
    titulo = 'FACTURAS'
    template = loader.get_template('facturas.html')
    lista_facturas = Factura.objects.select_related('reservacion_id').order_by('-identificador')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
        'lista_facturas' : lista_facturas,
    }
    return HttpResponse(template.render(context,request))