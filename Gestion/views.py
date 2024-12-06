from django.shortcuts import render, redirect
from django.http import HttpResponse
from Gestion.models import alumnos
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def busqueda_alumnos(request):
    return render(request, "busqueda_alumnos.html")

def buscar(request):
    if "alumnos" in request.GET:
        guardalum = request.GET["alumnos"]
        if len(guardalum)>50:
            mensaje= 'Texto de busqueda es demasiado largo, vuelve a intentar'
        else:
            buscar_alum = alumnos.objects.filter(nombre__icontains=guardalum)
            return render(request, "resultado_busqueda.html", {"alumnos": buscar_alum, "query": guardalum})
    else:
        mensaje = 'No haz capturado nada'
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=='POST':
        var_asunto= request.POST["asunto"]
        var_mensaje= request.POST["mensaje"] + " " + request.POST["email"]
        var_email_from= settings.EMAIL_HOST_USER
        receptor= ["miguel.hernandezmendoza@cesunbc.edu.mx"]
        send_mail(var_asunto, var_mensaje, var_email_from, receptor)
        return render(request, "gracias.html")
    return render(request, "contacto.html")

def Listar_Alumnos(request):
    alumno = alumnos.objects.all()
    return render(request, 'muestra_todos.html', {'alumno': alumno})

def registrar_alumno(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        direccion = request.POST['direccion']
        email = request.POST['email']
        telefono = request.POST['telefono']
        matricula = request.POST['matricula']

        try:
            nuevo_alumno = alumnos.objects.create(
                nombre = nombre,
                apellido = apellido,
                fecha_nacimiento = fecha_nacimiento,
                direccion = direccion,
                email = email,
                telefono = telefono,
                matricula = matricula,
            )
            return redirect('muestra_todos')
        except Exception as e:
            return HttpResponse(f"Error: {e}")
        
    return render(request, 'registrar_alumno.html')