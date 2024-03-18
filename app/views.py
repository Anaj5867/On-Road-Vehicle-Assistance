from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
# Create your views here.


class HomeView(TemplateView):
    template_name="home.html"

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.role = 'user'
        return super().form_valid(form)

class MechanicRegistrationView(CreateView):
    model = User
    form_class = MechanicRegistrationForm
    template_name = 'mechanic_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.role = 'mechanic'
        return super().form_valid(form)

class CarRenterRegistrationView(CreateView):
    model = User
    form_class = CarRenterRegistrationForm
    template_name = 'car_renter_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.role = 'car_renter'
        return super().form_valid(form)
    
class CarRenterHomeView(TemplateView):
    template_name="car_renter_home.html"

class UserHomeView(TemplateView):
    template_name="user_home.html"

class MechnaicHomeView(TemplateView):
    template_name="mechanic_home.html"


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            if user.role == 'mechanic':
                return redirect('mechanic_home')
            elif user.role == 'car_renter':
                return redirect('car_renter_home')
            else:
                return redirect('user_home')
        return super().form_invalid(form)


def LogoutView(request,*args,**kwargs):
    logout(request)
    return redirect("signin")  
