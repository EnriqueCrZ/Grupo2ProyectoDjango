from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import hashers


class SignupView(FormView):
    form_class = forms.SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        data = form.cleaned_data
        user = form.save(commit=False)
        user.password = hashers.make_password(data['password'])
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)


def Dashboard(request):
    return render(request, 'dashboard.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))


class LoginView(FormView):
    """login view"""

    form_class = forms.LoginForm
    success_url = reverse_lazy('index')
    template_name = 'login.html'

    def form_valid(self, form):
        credentials = form.cleaned_data

        user = authenticate(username=credentials['correo'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Credenciales incorrectas\
                                intente de nuevo')
            return HttpResponseRedirect(reverse_lazy('login'))
