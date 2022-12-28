from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns=[
    path('registro/',RegistroUsuarioApiView.as_view()),
    path('cines/',RegistroCineApiView.as_view()),
    path('salas/',RegistroSalaApiView.as_view()),

    path('registross/<int:pk>',RegistroUpdateApiView.as_view()),

    path('salas/<int:pk>',SalaDeleteApiView.as_view()),
    path('salass/',ListarSalasApiView.as_view()),

    path('salasss/<int:pk>',SalaUpdateApiView.as_view()),
    
    path('asientos/',RegistroAsientoApiView.as_view()),
    path('asientos-toggle/<str:id>',AsientoToggleApiView.as_view()),
    
    path('iniciar-sesion/',TokenObtainPairView.as_view()),
    path('sala-protegido/',VistaProtegidaApiView.as_view()),

    path('pelicula/',RegistroPeliculaApiView.as_view()),
    
]