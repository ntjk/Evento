from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Evento, Ponencia, Ponente, Fecha, Asistente
from django.utils import timezone


'''class IndexView(generic.ListView):
	template_name = 'eventos/index.html'
	context_object_name = 'lista_eventos'
	def get_queryset(self):
		return Evento.objects.order_by('-id'))'''
	
'''def ponentes(request):
    return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.all()})
    def get_queryset(self):
    	return Ponente.objects.filter()'''

def eventos(request):
	return render(request, 'eventos/index.html', {'eventos': Evento.objects.all()}) 

def ponencias(request, evento_id):
	if evento_id == 0:
		return render(request, 'eventos/ponencias.html', {'ponencias': Ponencia.objects.all()})
	else:
		return render(request, 'eventos/ponencias.html', {'ponencias': Ponencia.objects.filter(evento_id=evento_id)})

def ponentes(request, ponencia_id):
	if ponencia_id == 0:
		return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.all()})
	else:
		return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.filter(ponencia_id=ponencia_id)})

def fechas(request, evento_id):
	return render(request, 'eventos/fechas.html', {'fechas': Fecha.objects.filter(evento_id=evento_id)})

def asistentes(request, evento_id):
	return render(request, 'eventos/asistentes.html', {'asistentes': Asistente.objects.filter(evento_id=evento_id)})

def crearEvento(request):
	try:
		nombre = request.POST['firstname']
	except (KeyError, Evento.DoesNotExist):
		return render(request, 'eventos/crearEvento.html', {
			'error_message': "No ingreso nombre del evento",
		})
	else:
		nuevo_evento = Evento(nombre_evento = nombre)
		nuevo_evento.save()
	return HttpResponseRedirect(reverse('eventos:index'))