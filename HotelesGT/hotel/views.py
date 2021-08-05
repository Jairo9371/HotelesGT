from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

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

def hoteles(request):
    titulo = 'LISTA DE HOTELES'
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

def habitaciones(request):
    titulo = 'LISTADO DE HABITACIONES'
    template = loader.get_template('habitaciones.html')
    lista_habitacion = Habitacion.objects.all().order_by('-hotel_id')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
        'lista_habitacion' : lista_habitacion,
    }
    return HttpResponse(template.render(context,request))

def clientes(request):
    titulo = 'LISTADO DE CLIENTES'
    template = loader.get_template('clientes.html')
    lista_clientes = Cliente.objects.all().order_by('-nombre')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
        'lista_clientes' : lista_clientes,
    }
    return HttpResponse(template.render(context,request))

def reservaciones(request):
    titulo = 'LISTADO DE RESERVACIONES'
    template = loader.get_template('reservaciones.html')
    lista_reservaciones = Reservacion.objects.all().order_by('-estado')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
        'lista_reservaciones' : lista_reservaciones,
    }
    return HttpResponse(template.render(context,request))

def facturas(request):
    titulo = 'LISTADO DE FACTURAS'
    template = loader.get_template('facturas.html')
    lista_facturas = Factura.objects.all().order_by('-no_serie')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
        'lista_facturas' : lista_facturas,
    }
    return HttpResponse(template.render(context,request))