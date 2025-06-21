from django.contrib import admin
from django.urls import path
from aeropuerto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página de inicio
    path('aeropuertos/', views.lista_aeropuertos, name='lista_aeropuertos'),  # Lista de aeropuertos
    path('aeropuerto/agregar/', views.agregar_aeropuertos, name='agregar_aeropuertos'),
    path('aeropuerto/editar/<int:id>/', views.editar_aeropuertos, name='editar_aeropuertos'),
    path('aeropuerto/eliminar/<int:id>/', views.eliminar_aeropuertos, name='eliminar_aeropuertos'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
]


