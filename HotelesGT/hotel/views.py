from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    titulo = 'BIENVENIDOS AL INDEX'
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
    titulo = 'BIENVENIDOS A LOS HOTELES'
    template = loader.get_template('hoteles.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))

def habitaciones(request):
    titulo = 'BIENVENIDOS A LAS HABITACIONES'
    template = loader.get_template('habitaciones.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))

def clientes(request):
    titulo = 'BIENVENIDOS CLIENTES'
    template = loader.get_template('clientes.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))

def reservaciones(request):
    titulo = 'BIENVENIDOS A LAS RESERVACIONES'
    template = loader.get_template('reservaciones.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))

def facturas(request):
    titulo = 'BIENVENIDOS A LAS FACTURAS'
    template = loader.get_template('facturas.html')

    if request.method == "GET":
        print("METODO GET")
    
    if request.method == "POST":
        print("METODO POST")
    
    context = {
        'titulo' : titulo,
    }
    return HttpResponse(template.render(context,request))