from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Aeropuerto
from .forms import AeropuertoForm, RegistroUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method =='POST':
        form=RegistroUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegistroUserForm()
    
    return render(request, 'registro.html', {'form':form})

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario=request.POST['username']
        clave=request.POST['password']
        user=authenticate(request, username=usuario, password=clave)
        if user:
            login(request, user)
            return redirect('lista_aeropuertos')
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

#CRUD
@login_required

def lista_aeropuertos(request):
    aeropuerto=Aeropuerto.objects.all()
    return render(request, 'aeropuerto/lista.html', {'aeropuerto': aeropuerto})

@login_required

def agregar_aeropuertos(request):
    form=AeropuertoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_aeropuertos')
    return render(request, 'aeropuerto/form.html', {'form':form})

@login_required

def editar_aeropuertos(request, id):
    aeropuerto=Aeropuerto.objects.get(id=id)
    form=AeropuertoForm(request.POST or None, instance=aeropuerto)
    if form.is_valid():
        form.save()
        return redirect('lista_aeropuertos')
    return render(request,'aeropuerto/form.html', {'form': form})

@login_required

def eliminar_aeropuertos(request, id):
    aeropuerto=Aeropuerto.objects.get(id=id)
    aeropuerto.delete()
    return redirect('lista_aeropuertos')
