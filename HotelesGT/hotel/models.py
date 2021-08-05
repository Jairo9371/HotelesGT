from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.


class Pais(models.Model):
    """Modelo para guardar Paises"""
    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre País')
    codigo_area = models.IntegerField(blank = False, null = False, verbose_name = 'Código Área')

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name_plural = 'Países'

class Ciudad(models.Model):
    """Modelo para guardar Ciclass Meta:
        verbose_name_plural = 'País'udades"""
    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    nombre = models.CharField(max_length = 50, null = False, verbose_name = 'Nombre de la Ciudad')
    pais_id = models.ForeignKey(Pais, on_delete = models.PROTECT, verbose_name = "País")

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name_plural = 'Ciudades'

class Categoria(models.Model):
    """Modelo para manejo de Categoria de un Hotel"""
    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    nombre = models.IntegerField(blank = False, null = False, verbose_name = 'Nombre de la Categoria')

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name_plural = 'Categorías'

class Hotel(models.Model):

    """Modelo para guardar Hoteles"""

    identificador = models.AutoField(primary_key = True, verbose_name = 'Id')
    nombre = models.CharField(max_length = 100, null = False, verbose_name = 'Nombre')
    direccion = models.CharField(max_length = 100, null = False, verbose_name = 'Dirección')
    telefono = models.IntegerField(blank = False, null = False, verbose_name = 'Telefono')
    ciudad_id = models.ForeignKey(Ciudad, default = None, null = True, on_delete = models.PROTECT, verbose_name = 'Ciudad')
    categoria_id = models.ForeignKey(Categoria, default = None, null = True, on_delete = models.PROTECT, verbose_name = 'Categoria')
    usuario_id = models.ForeignKey(User, default = None, null = True, on_delete = models.PROTECT, verbose_name = 'Usuario')
    """Funcion para Retornar el Modelo"""

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.ciudad_id)
    
    class Meta:
        verbose_name_plural = 'Hoteles'


class Tipo_Habitacion(models.Model):
    """Modelo para manejar el tipo de habitación en el Hotel"""
    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    nombre = models.CharField(max_length = 25, null = False, verbose_name = 'Tipo Habitación')

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name_plural = 'Tipo de Habitaciones'
        verbose_name = 'Tipo de Habitación'


class Habitacion(models.Model):
    """Modelo para guardar las Habitaciones del Hotel"""

    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    hotel_id = models.ForeignKey(Hotel, on_delete = models.PROTECT, verbose_name = 'Hotel')
    tipo_id = models.ForeignKey(Tipo_Habitacion, on_delete = models.PROTECT, verbose_name = 'Tipo')
    description = models.CharField(max_length = 255, null = False, verbose_name = 'Descripción')
    precio = models.DecimalField(max_digits = 12, decimal_places = 2, verbose_name = 'Precio')
    usuario_id = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name = 'Usuario')

    def __str__(self):
        return '{} - {}'.format(self.description, self.precio)
    
    class Meta:
        verbose_name_plural = 'Habitaciones'

class Cliente(models.Model):
    """Modelo para guardar los clientes del Hotel"""

    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    nombre = models.CharField(max_length = 150, blank = False, null = False, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Apellido')
    nit = models.CharField(default = "C/F", max_length = 9, null = False, verbose_name = 'NIT')
    telefono = models.IntegerField(blank = True, null = True, verbose_name = 'Telefono')
    direccion = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Dirección')
    correo_electronico = models.EmailField(max_length = 80, default = None, null = True, verbose_name = 'Correo Electronico')
    contraseña = forms.CharField(widget = forms.PasswordInput, max_length = 50)
    
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
    
    class Meta:
        verbose_name_plural = 'Clientes'

class Reservacion(models.Model):
    """Modelo para guardar las reservaciones de cada clientes del Hotel"""

    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    fecha = models.DateField(auto_now = False, auto_now_add = False, verbose_name = 'Fecha de Reservación')
    cliente_id = models.ForeignKey(Cliente, on_delete = models.PROTECT, verbose_name = 'Cliente')
    hotel_id = models.ForeignKey(Hotel, on_delete = models.PROTECT, verbose_name = 'Hotel')
    description = models.CharField(max_length = 255, verbose_name = 'Descripción')
    usuario_id = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name = 'Usuario')
    estado = models.CharField(max_length =1, default ='A', null = True, blank = True, verbose_name = 'Estado' )

    def __str__(self):  
        return '{} - {}'.format(self.fecha, self.cliente_id)

    class Meta:
        verbose_name_plural = 'Reservaciones'

class Detalle_Reservacion(models.Model):
    """Modelo para guardar los detalles de las Reservaciones"""

    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    reservacion_id = models.ForeignKey(Reservacion, on_delete = models.PROTECT, verbose_name = 'Reservación')
    habitacion_id = models.ForeignKey(Habitacion, on_delete = models.PROTECT, verbose_name = 'Habitación')
    fecha_ingreso = models.DateField(auto_now = False, auto_now_add = False, verbose_name = 'Fecha de Ingreso')
    fecha_salida = models.DateField(auto_now = False, auto_now_add = False, verbose_name = 'Fecha de Salida')  
    nombre_reservacion = models.CharField(max_length = 60, blank = False, null = False, verbose_name = 'Nombre de la Reservación')

    def __str__(self):
        return 'Ingreso: {} - Salida: {}'.format(self.fecha_ingreso, self.fecha_salida)

    class Meta:
        verbose_name_plural = 'Detalles de Reservaciones'
        verbose_name = 'Detalle de Reservación'

class Factura(models.Model):
    """Modelo para guardar las facturas que hace el Hotel"""

    identificador = models.AutoField(primary_key=True, verbose_name = 'Id')
    no_serie = models.CharField(max_length = 15, blank = False, null = False, verbose_name = 'No. Serie')
    fecha = models.DateField(auto_now = False, auto_now_add = False, verbose_name = 'Fecha de la Factura')
    reservacion_id = models.ForeignKey(Reservacion, on_delete = models.PROTECT, verbose_name = 'Reservación')
    description = models.CharField(max_length = 255, null = False, verbose_name = 'Descripción')
    total = models.DecimalField(max_digits = 12, decimal_places = 2, verbose_name = 'Total')

    def __str__(self):
        return '{} - {} / {}'.format(self.no_serie, self. identificador, self.total)
    
    class Meta:
        verbose_name_plural = 'Facturas'

    



