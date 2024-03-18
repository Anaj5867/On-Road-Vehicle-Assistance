from django.urls import path
from .views import *
urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("user/home",UserHomeView.as_view(),name="user_home"),
    path("mechanic/home",MechnaicHomeView.as_view(),name="mechanic_home"),
    path("carRenter/home",CarRenterHomeView.as_view(),name="car_renter_home"),
    path("user/registration",UserRegistrationView.as_view(),name="user_registration"),
    path("mechanic/registration",MechanicRegistrationView.as_view(),name="mechanic_registration"),
    path("carrental/registration",CarRenterRegistrationView.as_view(),name="car_registration"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
]
