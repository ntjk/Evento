from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Evento, Ponencia, Ponente, Fecha, Asistente, User
from django.utils import timezone
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

'''class IndexView(generic.ListView):
	template_name = 'eventos/index.html'
	context_object_name = 'lista_eventos'
	def get_queryset(self):
		return Evento.objects.order_by('-id'))'''

def eventos(request):
	return render(request, 'eventos/index.html', {'eventos': Evento.objects.all()}) 

def ponencias(request, evento_id):
	if evento_id == 0:
		return render(request, 'eventos/ponencias.html', {'ponencias': Ponencia.objects.all(),
			#'evento':Evento.objects.filter(id=evento_id)[0]
			})
	else:
		return render(request, 'eventos/ponencias.html', {'ponencias': Ponencia.objects.filter(evento_id=evento_id),
			#'evento':Evento.objects.filter(id=evento_id)[0]
			})

def ponentes(request, ponencia_id):
	if ponencia_id == 0:
		return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.all()})
	else:
		return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.filter(ponencia_id=ponencia_id)})

def fechas(request, evento_id):
	return render(request, 'eventos/fechas.html', {'fechas': Fecha.objects.filter(evento_id=evento_id)})

def asistentes(request, evento_id):
	if evento_id == 0:
		return render(request, 'eventos/asistentes.html', {'asistentes': Asistente.objects.all()})
	else:
		return render(request, 'eventos/asistentes.html', {'asistentes': Asistente.objects.filter(evento_id=evento_id)})

def crearEvento(request):
	try:
		nombre = request.POST['nombre']
	except (KeyError, Evento.DoesNotExist):
		return render(request, 'eventos/crearEvento.html', {
			'error_message': "No ingreso nombre del evento",})
	else:
		nuevo_evento = Evento(nombre_evento = nombre)
		nuevo_evento.save()
	return HttpResponseRedirect(reverse('eventos:index'))

def crearPonencia(request):
	try:
		nombre = request.POST['nombre_ponencia']
		fecha = request.POST['fecha_ponencia']
		duracion = request.POST['duracion']
		evento = request.POST['evento']
		print(evento)
	except (KeyError, Evento.DoesNotExist):
		return render(request, 'eventos/crearPonencia.html', {
			'error_message': "No ingreso nombre del evento",
			'eventos': Evento.objects.all(),
			'ponentes': Ponente.objects.all()
			})
	else:
		nueva_ponencia = Ponencia(nombre_ponencia=nombre, fecha_ponencia=fecha, duracion=duracion,
			evento_id = evento)
		nueva_ponencia.save()
	return HttpResponseRedirect(reverse('eventos:ponencias', args=(0,)))

def agregarPonente(request):
	try:
		nombre = request.POST['nombre_ponente']
		apellido = request.POST['apellido_ponente']
		cargo = request.POST['cargo']
		organizacion = request.POST['organizacion_ponente']
		ponencia = request.POST['ponencia']
	except (KeyError, Ponente.DoesNotExist):
		return render(request, 'eventos/agregarPonente.html', {
			'error_message': "No ingreso datos del ponente",
			'ponencias': Ponencia.objects.all()
			})
	else:
		ponente = Ponente(nombre_ponente=nombre, apellido_ponente=apellido, cargo=cargo, 
			organizacion_ponente=organizacion, ponencia_id = ponencia)
		ponente.save()
	return HttpResponseRedirect(reverse('eventos:ponentes', args=(0,)))

def agregarAsistente(request):
	try:
		nombre = request.POST['nombre_asistente']
		apellido = request.POST['apellido_asistente']
		telefono = request.POST['telefono']
		email = request.POST['email']
		organizacion = request.POST['organizacion_asistente']
		evento = request.POST['evento']
	except (KeyError, Asistente.DoesNotExist):
		return render(request, 'eventos/agregarAsistente.html', {
			'error_message': "No ingreso datos del ponente",
			'eventos': Evento.objects.all(),
			})
	else:
		asistente = Asistente(nombre_asistente=nombre, apellido_asistente=apellido, telefono=telefono, 
			email=email, organizacion_asistente=organizacion, evento_id = evento)
		asistente.save()
	return HttpResponseRedirect(reverse('eventos:asistentes', args=(evento,)))

def agregarFecha(request):
	try:
		fecha = request.POST['fecha_evento']
		evento = request.POST['evento']
	except (KeyError, Fecha.DoesNotExist):
		return render(request, 'eventos/agregarFecha.html', {
			'error_message': "No ingreso fecha",
			'eventos': Evento.objects.all()})
	else:
		nueva_fecha = Fecha(fecha_evento = fecha, evento_id=evento)
		nueva_fecha.save()
	return HttpResponseRedirect(reverse('eventos:fechas', args=(evento,)))

'''def crearAgente(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'eventos/crearAgente.html', {'form': form})'''

def crearAgente(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			print('valido')
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect(reverse('eventos:index'))
	else:
		form = UserRegisterForm()
	return render(request, 'eventos/crearAgente.html', {'form' : form})