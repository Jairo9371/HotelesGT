from django.contrib import admin
from .models import *
# Register your models here.

#Acciones
@admin.action(description = "Quitar Número Telefónico")
def borrarTelefono(modeladmin, request, queryset):
    queryset.update(telefono=0)
    
@admin.action(description = "Cancelar Reservacion(es)")
def cambiarEstado(modeladmin, request, queryset):
    queryset.update(estado='C')

#Clases
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad_id', 'telefono')
    list_filter = ('ciudad_id',)
    search_fields = ('=identificador','nombre')

    actions = [borrarTelefono]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            del actions['borrarTelefono']
        return actions

class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_area')
    search_fields = ('=identificador','nombre')

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_id')
    search_fields = ('=identificador','nombre')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('identificador','nombre')
    search_fields = ('=identificador','nombre')

class TipoHAdmin(admin.ModelAdmin):
    list_display = ('identificador','nombre')
    search_fields = ('=identificador','nombre')

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('hotel_id','tipo_id','description', 'precio')
    list_filter = ('hotel_id', 'tipo_id',)
    search_fields = ('=identificador','hotel_id', 'tipo_id')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nit', 'telefono', 'direccion')
    search_fields = ('=identificador','nombre', 'apellido')

class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('fecha','cliente_id', 'hotel_id', 'description', 'usuario_id', 'estado')
    list_filter = ('cliente_id',)
    search_fields = ('=identificador','fecha', 'cliente_id', 'usuario_id')

    actions = [cambiarEstado]


class DetalleRAdmin(admin.ModelAdmin):
    list_display = ('reservacion_id','habitacion_id', 'fecha_ingreso', 'fecha_salida', 'nombre_reservacion')
    list_filter = ('reservacion_id', 'habitacion_id')
    search_fields = ('=identificador','nombre_reservacion', 'fecha_ingreso', 'fecha_salida')

class FacturAdmin(admin.ModelAdmin):
    list_display = ('no_serie','fecha', 'reservacion_id', 'description', 'total')
    list_filter = ('fecha',)
    search_fields = ('=identificador','no_serie', 'fecha', 'reservacion_id')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tipo_Habitacion, TipoHAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(Detalle_Reservacion, DetalleRAdmin)
admin.site.register(Factura, FacturAdmin)    






