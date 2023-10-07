"""
URL configuration for peliculas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from peliculas.views import prin
from gestionpeliculas.views import login,registarUsuario,Search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Principal/',prin,name="prin"),
    path('login/', login, name="login"),
    path('register/',registarUsuario, name='register'),
    path('listar_elementos/', Search, name='listar_elementos'),
    ##path('mostrar_elemento/<int:elemento_id>/', mostrar_elemento, name='mostrar_elemento'),
    

]
