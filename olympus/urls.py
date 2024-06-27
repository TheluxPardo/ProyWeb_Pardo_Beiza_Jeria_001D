from django.urls import path
from .views import inicio, login, quienessomos, galeria,agendar
from . import views
from .views import register_view, login_view

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('quienessomos/', views.quienessomos, name='quienessomos'),
    path('galeria/', views.galeria, name='galeria'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    path('sali/', views.salir, name='salir'),
    path('agendar/<str:corte>/', views.agendar, name='agendar'),

    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),
    path('reservas/<int:pk>/editar/', views.editar_reserva, name='editar_reserva'),
    path('reservas/<int:pk>/eliminar/', views.confirmar_eliminar, name='confirmar_eliminar'),

   
]