from django.shortcuts import render,get_object_or_404
from .models import Clientes, libros
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def login(request):
    if request.method == 'POST':
        try:
            detalleUsuario=Clientes.objects.get(usuario=request.POST['usuario'], password=request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['usuario']=detalleUsuario.usuario
            return render(request, "search.html")
        except Clientes.DoesNotExist as e:
            messages.success(request, 'No es correcto')
      
    return render(request, 'login.html')




def registarUsuario(request):
    if request.method == 'POST':
        usuario=request.POST['usuario']
        
        
        password=request.POST['password']
        
        Clientes(usuario=usuario, password=password).save()
        messages.success(request, 'el usuario'+request.POST['usuario']+ 'se registro correctamente')
        return render(request, 'Prin.html')
    else:
        return render(request, 'registrar.html')
    


def Search(request):
    query = request.GET.get("buscar")
    libro = libros.objects.all()
    if query:
        libro=libros.objects.filter(
            Q(autor__icontains=query)|
            Q(nombrelibro__icontains=query)
        
    
        ).distinct()
        
    
    return render(request, 'search.html', {'libro': libro})

        
    
    
    
def cerrarSesion(request):
    try:
        del request.session['usuario']
    except:
        return render(request,'Prin.html')
    return render(request,'Prin.html')


def mostrar_elemento(request, elemento_id):
    elemento = get_object_or_404(libros, pk=elemento_id)
    return render(request, 'mostrar_elemento.html', {'elemento': elemento})


    