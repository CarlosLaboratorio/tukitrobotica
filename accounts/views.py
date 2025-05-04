from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm, PerfilForm, EditarUsuarioForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Perfil

@login_required
def ver_perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def editar_perfil(request):
    user = request.user
    try:
        perfil = user.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(user=user)

    if request.method == 'POST':
        user_form = EditarUsuarioForm(request.POST, instance=user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
    
            # Cambiar contraseña si fue ingresada
            new_pass = user_form.cleaned_data.get("new_password1")
            if new_pass:
                user.set_password(new_pass)
            user.save()
    
            perfil_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('ver_perfil')
    else:
        user_form = EditarUsuarioForm(instance=user)
        perfil_form = PerfilForm(instance=perfil)

    return render(request, 'accounts/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  # Página de inicio
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'accounts/register.html', {'form': form})