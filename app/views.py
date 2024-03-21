from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.


class HomeView(TemplateView):
    template_name="home.html"

# class UserRegistrationView(CreateView):
#     model = User
#     form_class = UserRegistrationForm
#     template_name = 'user_register.html'
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         form.instance.role = 'user'
#         return super().form_valid(form)

# class MechanicRegistrationView(CreateView):
#     model = User
#     form_class = MechanicRegistrationForm
#     template_name = 'mechanic_register.html'
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         form.instance.role = 'mechanic'
#         return super().form_valid(form)

# class CarRenterRegistrationView(CreateView):
#     model = User
#     form_class = CarRenterRegistrationForm
#     template_name = 'car_renter_register.html'
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         form.instance.role = 'car_renter'
#         return super().form_valid(form)

class AdminRegistrationView(CreateView):
    model = User
    form_class = AdminRegistrationForm
    template_name = 'Admin_register.html'
    success_url = reverse_lazy('admin-login')

    # def form_valid(self, form):
    #     form.instance.role = form.cleaned_data['role']
    #     return super().form_valid(form)


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.role = form.cleaned_data['role']
        return super().form_valid(form)



class AdminHomeView(TemplateView):
    template_name="admin_home.html"

class CarRenterHomeView(TemplateView):
    template_name="car_renter_home.html"

class UserHomeView(TemplateView):
    template_name="user_home.html"

class MechnaicHomeView(TemplateView):
    template_name="mechanic_home.html"


class AdminLoginView(FormView):
    template_name = 'admin_login.html'
    form_class = LoginForm
    success_url = reverse_lazy('admin-home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.role == 'admin':
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid username or password for admin.')
            return self.form_invalid(form)

    def get_success_url(self):
        return self.success_url

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
    return redirect("home")  


class AddLocationView(CreateView):
    model=Location
    form_class=AddLocationForm
    template_name="add_location.html"
    success_url=reverse_lazy('admin-home')


class MechanicProfileAddView(CreateView):
    model = MechanicProfile
    form_class = MechanicProfileForm
    template_name = 'mechanic_profile_add.html'
    success_url = reverse_lazy('mechanic_home')

    def get_object(self, queryset=None):
        return MechanicProfile.objects.filter(user=self.request.user).first()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 
    

class MechanicProfileDetailView(DetailView):
    model = MechanicProfile
    template_name = 'mechanic_profile_view.html'
    context_object_name = 'data'

    def get_object(self, queryset=None):
        # Retrieve the MechanicProfile object for the current user
        return get_object_or_404(MechanicProfile, user=self.request.user)


class PendingMechanicView(ListView):
    model = MechanicProfile
    template_name = 'pending_mechanics_list.html'  # Replace 'pending_mechanics_list.html' with your actual template name
    context_object_name = 'data'

    def get_queryset(self):
        return MechanicProfile.objects.filter(status='pending')
    

def approve_mechanic(request, pk):
    mechanic_profile = get_object_or_404(MechanicProfile, pk=pk)
    if request.method == 'POST':
        mechanic_profile.status = 'approved'
        mechanic_profile.save()
        return redirect('pending-list')  # Redirect to the pending list page
    return redirect('pending-list')

class MechanicprofileUpdateView(UpdateView):
    model = MechanicProfile
    form_class = MechanicProfileForm
    template_name = 'mechanic_profile_update.html'
    success_url = reverse_lazy('mechanic_home')

    def get_object(self, queryset=None):
        return MechanicProfile.objects.get(user=self.request.user)

class UserProfileAddView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile_add.html'
    success_url = reverse_lazy('user_home')

    def get_object(self, queryset=None):
        return UserProfile.objects.filter(user=self.request.user).first()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 
    

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'user_profile_view.html'
    context_object_name = 'data'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user=self.request.user)
    
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile_update.html'
    success_url = reverse_lazy('user_home')

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)
    
class ApprovedMechanicListView(ListView):
    model = MechanicProfile
    template_name = 'approved_mechanic.html'
    context_object_name = 'mechanics'

    def get_queryset(self):
        return MechanicProfile.objects.filter(status='approved')

class ReqToMechanicCreateView(CreateView):
    model = ReqToMechanic
    form_class = ReqToMechanicForm
    template_name = 'create_req.html'
    success_url = reverse_lazy('user_requests')

    def form_valid(self, form):
        mechanic_id = self.kwargs.get('mechanic_id')
        mechanic = MechanicProfile.objects.get(pk=mechanic_id)
        form.instance.mechanic = mechanic
        # form.instance.user = self.request.user.userprofile
        form.instance.user = self.request.user.user_profile
        return super().form_valid(form)
    

class MechanicReqListView(ListView):
    model = ReqToMechanic
    template_name = 'mechanic_req_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        mechanic_profile = self.request.user.mechanic_profile
        return ReqToMechanic.objects.filter(mechanic=mechanic_profile)
    

def update_status(request, pk):
    req = get_object_or_404(ReqToMechanic, pk=pk)
    if request.method == 'POST':
        req.status = 'completed'
        req.save()
        return redirect('mechanic_requests')  # Redirect to the pending list page
    return redirect('mechanic_requests')



class UserRequestsListView(ListView):
    model = ReqToMechanic
    template_name = 'user_requests.html'
    context_object_name = 'user_requests'

    def get_queryset(self):
        return ReqToMechanic.objects.filter(user=self.request.user.user_profile)



class FeedBackCreateView(CreateView):
    model = FeedBack
    form_class = FeedBackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('user_requests')

    def form_valid(self, form):
        req_to_mechanic = get_object_or_404(ReqToMechanic, pk=self.kwargs['pk'])
        form.instance.user = self.request.user.user_profile
        form.instance.request = req_to_mechanic
        form.instance.mechanic_id = req_to_mechanic.mechanic.id
        return super().form_valid(form)
    
class FeedbackListView(ListView):
    model = FeedBack
    template_name = 'feedback_list.html'
    context_object_name = 'feedback_list'

    def get_queryset(self):
        mechanic_profile = self.request.user.mechanic_profile
        return FeedBack.objects.filter(mechanic=mechanic_profile)
    


class BillPaymentCreateView(CreateView):
    model = Bill
    form_class = BillPaymentForm
    template_name = 'create_bill.html'
    success_url = reverse_lazy('mechanic_requests')

    def form_valid(self, form):
        req_id = self.kwargs['pk']
        req = get_object_or_404(ReqToMechanic, pk=req_id)
        form.instance.req = req
        form.instance.mechanic = req.mechanic
        form.instance.customer = req.user
        payment_amount = form.cleaned_data['payment']
        return super().form_valid(form)
    


def bil_payment(request, pk):
    req = get_object_or_404(ReqToMechanic, pk=pk)
    bill = get_object_or_404(Bill, req=req)
    
    if request.method == 'POST':
        bill.status = 'completed'
        bill.save()
        return redirect('payment')  # Redirect to the pending list page
    return redirect('user_requests')


class PaymentSuccessView(TemplateView):
    template_name="payment_success.html"