from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .forms import CustomUserCreationForm, CustomLoginForm


class AuthView(View):
    def get(self, request):
        login_form = CustomLoginForm()
        register_form = CustomUserCreationForm()
        return render(request, 'accounts/inscription.html', {
            'login_form': login_form,
            'register_form': register_form
        })

    def post(self, request):
        if 'login' in request.POST:
            login_form = CustomLoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('shop:product_list')  # Redirigez vers la page d'accueil après la connexion
            return render(request, 'accounts/inscription.html', {'login_form': login_form, 'register_form': CustomUserCreationForm()})

        elif 'register' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('shop:product_list')  # Redirigez vers la page d'accueil après l'inscription
            return render(request, 'accounts/inscription.html', {'login_form': CustomLoginForm(), 'register_form': register_form})

        return redirect('auth')