
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),
    path('integrantes/', views.integrantes, name = "integrantes"),
    path('cursos/', views.cursos, name = "cursos"),
    path('agregarcurso/', views.formularioCurso, name = "agregarcurso"),
    path('recibircurso/', views.agregarCurso, name = "recibircurso"),
    path('carreras/', views.carreras , name = "carreras"),
    path('agregarcarrera/', views.agregarCarrera, name = "agregarcarrera")
]
