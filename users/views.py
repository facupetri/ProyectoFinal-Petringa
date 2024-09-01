from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from users.models import Avatar
from users.forms import UserRegisterForm, UserEditForm
from django.urls import reverse_lazy

def login_request(request):
    msg_error = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return render(request, 'base/index.html')
        msg_error = 'Usuario o contraseña incorrecta!'

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'msg_error': msg_error})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base/index.html', {'mensaje': 'Usuario creado con exito!'})
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def edit_user(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if mi_formulario.is_valid():
            mi_formulario.save()

            imagen = mi_formulario.cleaned_data.get('imagen')
            if imagen:
                avatar, created = Avatar.objects.get_or_create(user=usuario)
                avatar.imagen = imagen
                avatar.save()

            return render(request, 'base/index.html')

    else:
        mi_formulario = UserEditForm(instance=request.user)

    return render(request, 'users/edit_user.html', {'form': mi_formulario})


class CambiarContrasena(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/change_pass.html'
    success_url = reverse_lazy('edit_user')