from django.contrib import admin
from .models import Cliente, Credito, Banco

# Registrando los modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Credito)
admin.site.register(Banco)
