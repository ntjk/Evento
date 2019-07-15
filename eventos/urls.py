from django.urls import path
from . import views
app_name = 'eventos'


urlpatterns = [
	#path('', views.IndexView.as_view(), name='index'),
	path('', views.eventos, name='index'),
	path('<int:evento_id>/ponencias', views.ponencias, name='ponencias'),
	path('<int:evento_id>/asistentes', views.asistentes, name='asistentes'),
	path('<int:evento_id>/fechas', views.fechas, name='fechas'),
	path('<int:ponencia_id>/ponentes', views.ponentes, name='ponentes'),
	path('crearEvento', views.crearEvento, name='crearEvento'),
	path('crearPonencia', views.crearPonencia, name='crearPonencia'),
	path('agregarPonente', views.agregarPonente, name='agregarPonente'),
	path('agregarAsistente', views.agregarAsistente, name='agregarAsistente'),
	path('agregarFecha', views.agregarFecha, name='agregarFecha'),
	path('crearGerente', views.agregarFecha, name='agregarFecha'),
	path('crearAgente', views.crearAgente, name='crearAgente'),
	#path('<int:pk>/', views.DetalleView.as_view(), name='detalle'),
	#path('<int:pk>/ponencias/', views.PonenciasView.as_view(), name='ponencias'),
	#path('', views.index, name='index'),
	#path('<int:question_id>/', views.detail, name='detail'),
]