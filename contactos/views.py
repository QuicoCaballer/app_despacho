from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Contacto

CAMPOS = ["nombre", "apellidos", "tipo", "email", "telefono", "direccion", "notas"]


class ContactoListView(LoginRequiredMixin, ListView):
    model = Contacto
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        tipo = self.request.GET.get("tipo", "")
        if q:
            qs = qs.filter(
                Q(nombre__icontains=q)
                | Q(apellidos__icontains=q)
                | Q(email__icontains=q)
                | Q(telefono__icontains=q)
            )
        if tipo:
            qs = qs.filter(tipo=tipo)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["q"] = self.request.GET.get("q", "").strip()
        ctx["tipo_actual"] = self.request.GET.get("tipo", "")
        ctx["tipos"] = Contacto.Tipo.choices
        return ctx


class ContactoCreateView(LoginRequiredMixin, CreateView):
    model = Contacto
    fields = CAMPOS
    success_url = reverse_lazy("contactos:lista")


class ContactoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contacto
    fields = CAMPOS
    success_url = reverse_lazy("contactos:lista")


class ContactoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contacto
    success_url = reverse_lazy("contactos:lista")
