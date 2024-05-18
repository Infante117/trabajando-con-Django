from django.shortcuts import render,redirect #importamos render y redirect de django.shortcuts, 
from django.http import HttpResponse #importamos HttpResponse, 
                    #que nos permite devolver una respuesta a una petición HTTP
from .models import Libro #importamos el modelo Libro
from .forms import LibroForm #importamos el formulario LibroForm

#def inicio(request):#creamos una funcion que recibe un request
#    return HttpResponse("<h1>Inicio</h1>") #retornamos un HttpResponse con un h1
def inicio(request):
    return render(request, 'paginas/inicio.html') #retornamos un render con la plantilla inicio.html
def nosotros(request):
    return render(request, 'paginas/nosotros.html') #retornamos un render con la plantilla nosotros.html
def libros(request):
    libros=Libro.objects.all() #obtenemos todos los libros de la base de datos
    return render(request, 'paginas/libros/index.html',{'libros':libros}) #retornamos un render con la plantilla libros.html
def crear(request):
    formulario=LibroForm(request.POST or None, request.FILES or None) #creamos un formulario de LibroForm, 
                                                                    #y le pasamos el request.POST que contiene los datos del formulario
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')                                                               
    return render(request, 'paginas/libros/crear.html',{'formulario':formulario}) #retornamos un render con la plantilla crear.html, 
                                                                                    #y le pasamos el formulario como contexto 
def editar(request,id):
    #recuperamos el libro por el id
    libro = Libro.objects.get(idlibro=id)
    formulario=LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')  
    return render(request, 'paginas/libros/editar.html',{'formulario':formulario}) #retornamos un render con la plantilla editar.html
def eliminar(request,id):
    libro = Libro.objects.get(idlibro=id) #obtenemos el libro por el id
    libro.delete() #eliminamos el libro
    return redirect('libros') #redireccionamos a la vista libros
    
