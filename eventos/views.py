from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Evento, Ponencia, Ponente, Fecha, Asistente, User, Registro_usuario
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import AgenteRegisterForm, GerenteRegisterForm, AdminRegisterForm
from django.contrib.auth.decorators import login_required
import datetime

'''Notas general: @login_required hace que la funcion sobre la que se coloca, requiera que el usuario
	haya iniciado sesion para que pueda suceder. Si no, lo redirige a la ruta indicada en
	el argumento login_url'''

#VISTAS QUE MUESTRAN TABLAS INFORMATIVAS SOBRE LOS EVENTOS: FECHAS, PONENCIAS, PONENETES Y ASISTENTES
@login_required(login_url='login')
def eventos(request):
	return render(request, 'eventos/index.html', {'eventos': Evento.objects.all()}) 

@login_required(login_url='login')
def ponencias(request, evento_id):
	if evento_id == 0:
		return render(request, 'eventos/ponencias.html', {'ponencias': Ponencia.objects.all(),})
	else:
		return render(request, 'eventos/ponencias.html', {'ponencias': Ponencia.objects.filter(evento_id=evento_id),})

@login_required(login_url='login')
def ponentes(request, ponencia_id):
	if ponencia_id == 0:
		return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.all()})
	else:
		return render(request, 'eventos/ponentes.html', {'ponentes': Ponente.objects.filter(ponencia_id=ponencia_id)})

@login_required(login_url='login')
def fechas(request, evento_id):
	return render(request, 'eventos/fechas.html', {'fechas': Fecha.objects.filter(evento_id=evento_id)})

@login_required(login_url='login')
def asistentes(request, evento_id):
	if evento_id == 0:
		return render(request, 'eventos/asistentes.html', {'asistentes': Asistente.objects.all()})
	else:
		return render(request, 'eventos/asistentes.html', {'asistentes': Asistente.objects.filter(evento_id=evento_id)})

@login_required(login_url='login')
def auditoria(request):
	if request.user.user_type == 'Administrador':
		return render(request, 'eventos/auditoria.html', {'auditoria': Registro_usuario.objects.all()})
	else:
		return HttpResponseRedirect(reverse('eventos:index'))

#VISTAS PARA AGREGAR INFORMACION EN LA BD SOBRE LOS EVENTOS: FECHAS, PONENCIAS, PONENETES Y ASISTENTES
@login_required(login_url='login')
def crearEvento(request):
	if request.user.user_type == 'Gerente':
		try:
			nombre = request.POST['nombre']
		except (KeyError, Evento.DoesNotExist):
			return render(request, 'eventos/crearEvento.html', {
				'error_message': "No ingreso nombre del evento",})
		else:
			nuevo_evento = Evento(nombre_evento = nombre)
			nuevo_evento.save()
		return HttpResponseRedirect(reverse('eventos:index'))
	else:
		return HttpResponseRedirect(reverse('eventos:index'))

@login_required(login_url='login')
def crearPonencia(request):
	if request.user.user_type == 'Gerente':
		try:
			nombre = request.POST['nombre_ponencia']
			fecha = request.POST['fecha_ponencia']
			hora = request.POST['hora']
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
			nueva_ponencia = Ponencia(nombre_ponencia=nombre, fecha_ponencia=fecha, hora=hora, duracion=duracion,
				evento_id = evento)
			nueva_ponencia.save()
		return HttpResponseRedirect(reverse('eventos:ponencias', args=(0,)))
	else:
		return HttpResponseRedirect(reverse('eventos:ponencias', args=(0,)))

@login_required(login_url='login')
def agregarPonente(request):
	if request.user.user_type == 'Gerente':
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
	else:
		return HttpResponseRedirect(reverse('eventos:ponentes', args=(0,)))

@login_required(login_url='login')
def agregarAsistente(request):
	if request.user.user_type == 'Agente':
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
	else:
		return HttpResponseRedirect(reverse('eventos:index'))

@login_required(login_url='login')
def agregarFecha(request):
	if request.user.user_type == 'Gerente':
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
	else:
		return HttpResponseRedirect(reverse('eventos:fechas', args=(evento,)))

# Funcion que guarda el registro sobre la creacion de usuarios, se llama cada vez que se cree uno
def auditar(request):
	print ('auditar')
	ultimo = User.objects.order_by('-id')[0]
	nuevo_registro = Registro_usuario(fecha_registro = datetime.date.today(), 
		hora_registro = datetime.datetime.now().time(),
		id_creador = request.user.id, usuario = ultimo)
	nuevo_registro.save()

#VISTAS PARA AGREGAR USUARIOS DE ACUERDO A SU ROL
@login_required(login_url='login')
def crearAgente(request):
	if request.user.user_type == 'Administrador':
		if request.method == 'POST':
			form = AgenteRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Account created for {username}!')
				auditar(request)
				return redirect(reverse('eventos:index'))
		else:
			form = AgenteRegisterForm()
		return render(request, 'eventos/crearUsuario.html', {'form' : form})
	else:
		return HttpResponseRedirect(reverse('eventos:index'))

@login_required(login_url='login')
def crearGerente(request):
	if request.user.user_type == 'Administrador':
		if request.method == 'POST':
			form = GerenteRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Account created for {username}!')
				auditar(request)
				return redirect(reverse('eventos:index'))
		else:
			form = GerenteRegisterForm()
		return render(request, 'eventos/crearUsuario.html', {'form' : form})
	else:
		return HttpResponseRedirect(reverse('eventos:index'))

@login_required(login_url='login')
def crearAdministrador(request):
	if request.user.user_type == 'Administrador':
		if request.method == 'POST':
			form = AdminRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Account created for {username}!')
				auditar(request)
				return redirect(reverse('eventos:index'))
		else:
			form = AdminRegisterForm()
		return render(request, 'eventos/crearUsuario.html', {'form' : form})
	else:
		return HttpResponseRedirect(reverse('eventos:index'))