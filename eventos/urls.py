from django.urls import path
from . import views
app_name = 'eventos'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('ponencias', views.ponencias, name='ponencias'),
	#path('<int:pk>/', views.DetalleView.as_view(), name='detalle'),
	#path('<int:pk>/ponencias/', views.PonenciasView.as_view(), name='ponencias'),
	#path('', views.index, name='index'),
	#path('<int:question_id>/', views.detail, name='detail'),
]