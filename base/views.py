from django.shortcuts import render, redirect
from.Carrito import Carrito
from.models import Comment, Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {'productos' : productos}
    return render (request, 'home.html', data)


def loginPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión correcto')
                return redirect('/')
        messages.error(request, 'Datos incorrectos')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/#/')

def registerPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El usuario ya existe')
            else:
                user = User.objects.create_user(username, email, password, first_name=name)
                user.save()
                messages.success(request, 'Usuario creado correctamente')
                return redirect('/login')
    return render(request,'register.html')

def acerca (request):
    return render(request, 'acerca.html')

def agregarproducto(request, id  = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if (id is None):
            Producto.objects.create(
                title = request.POST.get('title', None),
                content = request.POST.get('content', None),
                precio = request.POST.get('precio', None),
                imagen = request.POST.get('imagen', None),
                user = request and request.user
            )
            messages.success(request, 'Producto creado correctamente')
            return redirect('/')
        else:
            p = Producto.objects.get(id = id)
            if(p.user == request.user):
                p.title = request.POST.get('title', None)
                p.content = request.POST.get('content', None)
                p.save()

    context = {}
    if id is not None:
      p = Producto.objects.get(id = id)
      context['post'] = p
        
    return render(request, 'agregarproducto.html',context)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregar(producto)
    return redirect ("home/")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("home")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect ("home")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpir()
    return redirect("home")

