from django.db import models

# Create your models here.
#Tabla Alumnos
class alumnos (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)
    matricula = models.CharField(max_length=20, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

#Tabla de profesores
class profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    

#Tabla de cursos
class curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    profesor = models.ForeignKey(profesores, on_delete=models.SET_NULL, null=True, related_name='curso')

    def __str__(self):
        return self.nombre
    

#Tabla de inscripciones a los cursos
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(alumnos, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('estudiante', 'curso')  

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.curso}"

