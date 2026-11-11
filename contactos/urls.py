from django.urls import path

from . import views

app_name = "contactos"

urlpatterns = [
    path("", views.ContactoListView.as_view(), name="lista"),
    path("nuevo/", views.ContactoCreateView.as_view(), name="crear"),
    path("<int:pk>/editar/", views.ContactoUpdateView.as_view(), name="editar"),
    path("<int:pk>/borrar/", views.ContactoDeleteView.as_view(), name="borrar"),
]
