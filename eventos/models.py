from django.db import models

class Evento(models.Model):
	nombre_evento = models.CharField('Nombre', max_length=100)
	#asistentes = models.ManyToManyField(Asistente)
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
	fecha_ponencia = models.DateTimeField('Fecha')
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