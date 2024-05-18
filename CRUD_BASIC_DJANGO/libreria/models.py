from django.db import models

# nos sirve para capturar toda la estructura de la tabla
class Libro(models.Model):
    idlibro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name='Titulo del libro')
    portada = models.ImageField(upload_to='imagenes/',verbose_name='Portada del libro')
    autor = models.CharField(max_length=100,verbose_name='Autor del libro')
    editorial = models.CharField(max_length=100,verbose_name='Editorial del libro')
    fecha_publicacion = models.DateField(verbose_name='Fecha de publicacion del libro')
    
    def __str__(self): #nos sirve para mostrar los datos de la tabla
        fila = "Titulo: " + self.titulo + " -" +" Autor: " + self.autor + " -" +" Editorial: " + self.editorial + " -" +" Fecha de publicacion: " + str(self.fecha_publicacion)
        return fila
    
    def delete(self,using=None,keep_parents=False):#nos sirve para eliminar la imagen de la carpeta imagenes
        self.portada.storage.delete(self.portada.name)#elimina la imagen de la carpeta imagenes
        super().delete()#elimina el registro de la tabla

    
