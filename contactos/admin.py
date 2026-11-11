from django.contrib import admin

from .models import Contacto


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "tipo", "email", "telefono")
    list_filter = ("tipo",)
    search_fields = ("nombre", "apellidos", "email", "telefono")
