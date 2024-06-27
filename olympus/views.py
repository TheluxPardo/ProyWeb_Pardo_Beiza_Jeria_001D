from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva, Servicio
from .forms import ReservaForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .forms import CustomUserCreationForm, ReservaForm  # Asegúrate de importar correctamente


# Create your views here.
def inicio(request):
    return render(request, 'Inicio.html')

def index(request):
    return render(request, 'index.html')


def quienessomos(request):
    return render(request, 'QuienesSomos.html')


def galeria(request):
    return render(request, 'Galeria.html')

def salir(request):
    logout(request)
    return redirect('/')

@login_required
def agendar(request, corte):
    if request.method == "POST":
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        
    
        messages.success(request, '¡Agendamiento exitoso!')
        return redirect('inicio')
    
    return render(request, 'agendar.html', {'corte': corte})
#----------------------------------------

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
#----------------------------------------------------------------------------
@login_required
def lista_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'lista_reservas.html', {'reservas': reservas})

@login_required
def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'detalle_reserva.html', {'reserva': reserva})

@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form})

@login_required
def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form})

@login_required
def confirmar_eliminar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'confirmar_eliminar.html', {'reserva': reserva})

