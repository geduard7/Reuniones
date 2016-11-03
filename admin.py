from django.contrib import admin
#from App.models import Lugar, Area, Citacion, Asistente, Tema, Acta, Tarea
#from .views import citaciones, actas, lugares, areas
from App.models import Reuniones, TipoReunion, EstadoReunion, Lugar
from .views import FormularioReuniones, tiposreuniones, lugares, estadosreuniones
#Administracion
admin.site.register(Lugar, lugares)
admin.site.register(TipoReunion, tiposreuniones)
admin.site.register(EstadoReunion, estadosreuniones)
#admin.site.register(Citacion, citaciones)
#admin.site.register(Acta, actas)
# Register your models here.
admin.site.register(Reuniones, FormularioReuniones)