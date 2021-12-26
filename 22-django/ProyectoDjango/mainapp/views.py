from django.shortcuts import render, redirect # redirect para redirigir a otra pagina
from django.contrib import messages # Msj flash en el formulario de registro
from django.contrib.auth.forms import UserCreationForm # Para usar la app de autentificación
from mainapp.forms import RegisterForm # Para usar la clase de forms.py
from django.contrib.auth import authenticate, login, logout # Autentificación, login y logout

# Create your views here.

# Vistas de la app principal

def index(request): # Inicio

    # Pasar datos desde la vista y mostrarlos en la plantilla
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request): # Sobre nosotros

    # Pasar datos desde la vista y mostrarlos en la plantilla
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros'
    })

def register_page(request): # Registro con formulario

    # Evita que pueda acceder al http://localhost:8000/registro/ estando autenticado
    if request.user.is_authenticated: # Si el usuario esta autenticado
        return redirect('inicio')

    else: # Sino, tiene que registrarse

        # Crea formulario de registro de usuarios
        #register_form = UserCreationForm()
        # Usar formulario personalizado
        register_form = RegisterForm()

        # Comprobar si llega el metodo POST (significa que el formulario se ha enviado)
        if request.method == 'POST':
            # request.POST = Pasa los datos del formulario 
            # (en el caso de no colocar nada lo rellena automaticamente)
            #register_form = UserCreationForm(request.POST)
            register_form = RegisterForm(request.POST)

            # Si el formulario es valido
            if register_form.is_valid():
                # Guarda ese formulario
                register_form.save()

                # Msj. flash
                messages.success(request, 'Te has registrado correctamente!!')

                # Redirige a otra pagina
                return redirect('inicio')

        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request): # Login de usuario

    # Evita que pueda acceder al http://localhost:8000/login/ estando autenticado
    if request.user.is_authenticated: # Si el usuario esta autenticado
        return redirect('inicio')

    else: # Sino, tiene que iniciar sesión

        # Comprobar que nos llegue por POST los datos del formulario
        if request.method == 'POST':
            # Recoger datos
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Creo objeto (DatosKeywordArgument=DatosIntroducidosUsuario)
            user = authenticate(request, username=username, password=password)

            # Si la autentificación es correcta
            if user is not None: # Si es diferente a None el usuario, quiere decir que es correcto
                login(request, user)

                # Redirige a la pagina de inicio
                return redirect('inicio')
            else: # Si es igual a None
                # Muestra msj. flash
                messages.warning(request, 'No te has identificado correctamente :(')

        return render(request, 'users/login.html',{
            'title': 'Identificate'
        })

def logout_user(request): # Cerrar sesión

    # Automaticamente sabe que usuario desloguear
    logout(request)

    # Redirige al login
    return redirect('login')