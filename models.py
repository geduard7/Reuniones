from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Clase para crear la tabla de tipos de reunion.
SINO = (
		('S', 'Disponible'),
		('N', 'No Disponible'),
	)

class TipoReunion(models.Model):
	idTipo = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=50)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

	def __unicode__(self): # __str__ on Python 3
		return str(self.descripcion)

#Clase para crear la tabla de Lugares de la reunion.
class Lugar(models.Model):
	
	idLugar = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=50)
	Estado = models.CharField(max_length=1,choices=SINO, null=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)


	def __unicode__(self): # __str__ on Python 3
		return str(self.descripcion)

#Clase para crear la tabla de Estado de la reunion.
class EstadoReunion(models.Model):
	idEstado = models.AutoField(primary_key=True)
	NombreEstado = models.CharField(max_length=100)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)


	def __unicode__(self): # __str__ on Python 3
		return str(self.NombreEstado)

#Clase para crear la tabla de Estado de la tarea.
class EstadoTarea(models.Model):
	IdEstadoTarea = models.AutoField(primary_key=True)
	NomEstadoTar = models.CharField(max_length=100, null=True, blank=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

class Reuniones(models.Model):

	CANTIDADHORAS = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
	)
	IdReunion = models.AutoField(primary_key=True, verbose_name="Numero de Citacion")
	organizador = models.CharField(max_length=50)
	fecha_hora = models.DateTimeField()
	tiempo_estimado = models.CharField(max_length=1, null=True, choices=CANTIDADHORAS, help_text='Numero de Horas')
	asunto = models.CharField(max_length=100)
	idTipo = models.ForeignKey(TipoReunion, on_delete=models.CASCADE, null=True)
	idLugar = models.ForeignKey(Lugar, on_delete=models.CASCADE, null=True)
	hora_final = models.TimeField(help_text='HH24:MM:SS')
	idEstado = models.ForeignKey(EstadoReunion,on_delete=models.CASCADE, max_length=2)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

	def __unicode__(self): # __str__ on Python 3
		return str(self.IdReunion)

	def __init__(self, *args, **kwargs):
		super(Reuniones, self).__init__(*args, **kwargs)
		self.__total__ = None

class Tema(models.Model):
	id = models.AutoField(primary_key=True)
	idTema = models.ManyToManyField(Reuniones, related_name='Temas')
	NombreTema = models.CharField(max_length=500, null=True)
	Contenido = models.TextField(max_length=4000, null=True)
	Acuerdos = models.TextField(max_length=4000, null=True)
