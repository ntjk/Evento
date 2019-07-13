from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Evento, Ponencia, Ponente, Fecha, Asistente
from django.utils import timezone


class IndexView(generic.ListView):
	template_name = 'eventos/index.html'
	context_object_name = 'lista_eventos'
	def get_queryset(self):
		return Evento.objects.order_by('-id')#.filter(pub_date__lte=timezone.now())

'''def ponentes(request):
    return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.all()})
    def get_queryset(self):
    	return Ponente.objects.filter()'''

def ponencias(request):
    return render(request, 'eventos/ponencias.html', {'ponencias': Ponencia.objects.all()})