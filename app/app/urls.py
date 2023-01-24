"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include


from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', views.index),
    path('acercade', views.acercade),
    path('api', views.api),
    path('galeria', views.galeria),
    path('Registro2', views.Registro2),
    path('formulario1', views.formulario1),
    path('registrarUsuario', views.registrarUsuario),
    path('formulario3', views.registro3)
]
