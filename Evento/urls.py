from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from eventos import views as eventos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # se usa include para hacer referencia al archivo URLConfig de la aplicacion de eventos
    path('', include('eventos.urls')),
    # se hace uso de la libreria que trae Django por defecto para hacer el login y el logout
    # as_view permite que se utilicen vistas propias en vez de las que trae por defecto esa libreria
    path('login/', auth_views.LoginView.as_view(template_name='eventos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='eventos/logout.html'), name='logout'),
]