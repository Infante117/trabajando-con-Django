from django.urls import path
from .import views #importamos las vistas de la aplicación
from django.conf import settings #importamos settings de django, que nos permite acceder a las configuraciones del proyecto
from django.contrib.staticfiles.urls import static #importamos static de django.contrib.staticfiles.urls, que nos permite acceder a los archivos estaticos


urlpatterns = [#aqui el usuario podrá acceder a la urls de la aplicación
    path('', views.inicio, name='inicio'), #definimos la url de inicio
    path('nosotros/', views.nosotros, name='nosotros'), #definimos la url de nosotros
    path('libros/', views.libros, name='libros'), #definimos la url de libros
    path('libros/crear/', views.crear, name='crear'), #definimos la url de crear
    path('libros/editar/<int:id>/', views.editar, name='editar'), #definimos la url de editar
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'), #definimos la url de eliminar con un parametro id de tipo entero
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #accedemos a los archivos estaticos
