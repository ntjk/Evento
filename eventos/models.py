from django.db import models
from django.contrib.auth.models import AbstractUser

'''Hereda de AbstractUser para utilizar todo lo que tiene el usuario por defecto de Django.
Campos listos, compatibilidad con aplicaciones de Django, etc. Aqui lo extendemos para 
poder agregarle los campos user_type y phone. Este modelo englobará los tres perfiles
que se piden: administrador, gerente y agente'''
class User(AbstractUser):
	#user_type es el atributo que nos permite saber el rol del usuario.
    user_type = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)

# Modelo que permite realizar la auditoria
class Registro_usuario(models.Model):
	fecha_registro = models.DateField()
	hora_registro = models.TimeField()
	id_creador = models.IntegerField()
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)

'''Los siguientes modelos representan la información de interés de la aplicación
Se utiliza def __str__ en todos para que dicho objeto tenga su representacion en string'''
class Evento(models.Model):
	nombre_evento = models.CharField('Nombre', max_length=100)
	def __str__(self):
		return self.nombre_evento
		
class Asistente(models.Model):
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
	nombre_asistente = models.CharField('Nombre', max_length=50)
	apellido_asistente = models.CharField('Apellido', max_length=50)
	telefono = models.CharField(max_length=12)
	email = models.CharField(max_length=70)
	organizacion_asistente = models.CharField('Organización a la que pertenece', max_length=65)
	def __str__(self):
		return self.nombre_asistente+' '+self.apellido_asistente

class Fecha(models.Model):
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
	fecha_evento = models.DateField('Fecha')
	def __str__(self):
		return str(self.fecha_evento)

class Ponencia(models.Model):
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
	nombre_ponencia = models.CharField('Nombre', max_length=100)
	fecha_ponencia = models.DateField('Fecha')
	hora = models.TimeField()
	duracion = models.CharField(max_length=9)
	def __str__(self):
		return self.nombre_ponencia

class Ponente(models.Model):
	ponencia = models.OneToOneField(Ponencia, on_delete=models.CASCADE)
	nombre_ponente = models.CharField('Nombre', max_length=50)
	apellido_ponente = models.CharField('Apellido', max_length=50)
	cargo = models.CharField(max_length=50)	
	organizacion_ponente = models.CharField('Organización a la que pertenece', max_length=65)
	def __str__(self):
		return self.nombre_ponente+' '+self.apellido_ponente