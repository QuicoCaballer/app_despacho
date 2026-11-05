from django.db import models


class Contacto(models.Model):
    class Tipo(models.TextChoices):
        CLIENTE = "cliente", "Cliente"
        PROCURADOR = "procurador", "Procurador"
        JUZGADO = "juzgado", "Juzgado"
        PARTE_CONTRARIA = "parte_contraria", "Parte contraria"
        PERITO = "perito", "Perito"
        OTRO = "otro", "Otro"

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150, blank=True)
    tipo = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.CLIENTE)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    direccion = models.TextField(blank=True)
    notas = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["apellidos", "nombre"]
        verbose_name_plural = "contactos"

    def __str__(self):
        return f"{self.nombre} {self.apellidos}".strip()