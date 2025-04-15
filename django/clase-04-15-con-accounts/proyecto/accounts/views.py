from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

    
    
class UserRegisterView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')


class UserLoginView(LoginView):

    template_name = 'accounts/login.html'

