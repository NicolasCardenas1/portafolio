from django.contrib import admin
from .models import Categoria, Tecnologia, Proyecto

#Registro de modelos en el panel de administracion

admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Proyecto)

# Register your models here.
