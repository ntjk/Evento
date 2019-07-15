from django.contrib import admin
from .models import Evento, Fecha, Ponencia, Ponente, Asistente, User, Registro_usuario

admin.site.register(User)
admin.site.register(Evento)
admin.site.register(Fecha)
admin.site.register(Ponencia)
admin.site.register(Ponente)
admin.site.register(Asistente)
admin.site.register(Registro_usuario)