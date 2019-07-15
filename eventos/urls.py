from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User 
app_name = 'eventos'

urlpatterns = [
	# Pagina principal, se ve el menu y los eventos disponibles
	path('', views.eventos, name='index'),
	# Muestra las ponencias del evento cuyo id sea evento_id
	path('<int:evento_id>/ponencias', views.ponencias, name='ponencias'),
	# Muestra los asistentes del evento cuyo id sea evento_id
	path('<int:evento_id>/asistentes', views.asistentes, name='asistentes'),
	# Muestra las fechas del evento cuyo id sea evento_id
	path('<int:evento_id>/fechas', views.fechas, name='fechas'),
	# Muestra el ponente de la ponencia cuyo id sea ponencia_id
	path('<int:ponencia_id>/ponentes', views.ponentes, name='ponentes'),
	path('crearEvento', views.crearEvento, name='crearEvento'),
	path('crearPonencia', views.crearPonencia, name='crearPonencia'),
	path('agregarPonente', views.agregarPonente, name='agregarPonente'),
	path('agregarAsistente', views.agregarAsistente, name='agregarAsistente'),
	path('agregarFecha', views.agregarFecha, name='agregarFecha'),
	path('crearAdministrador', views.crearAdministrador, name='crearAdministrador'),
	path('crearGerente', views.crearGerente, name='crearGerente'),
	path('crearAgente', views.crearAgente, name='crearAgente'),
	# Muestra los administradores, gerentes y agentes creados, la fecha y hora asi como id del creador
	path('auditoria', views.auditoria, name='auditoria'),
]