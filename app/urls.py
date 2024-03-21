from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("user/home",AdminHomeView.as_view(),name="admin-home"),
    path("user/home",UserHomeView.as_view(),name="user_home"),
    path("mechanic/home",MechnaicHomeView.as_view(),name="mechanic_home"),
    path("carRenter/home",CarRenterHomeView.as_view(),name="car_renter_home"),
    path("user/registration",RegistrationView.as_view(),name="user_registration"),
    path("register/admin",AdminRegistrationView.as_view(),name="admin-registration"),
    path('login/admin', AdminLoginView.as_view(), name='admin-login'),
    path('pending',PendingMechanicView.as_view(),name="pending-list"),
    path('approval/<int:pk>',approve_mechanic,name="approve"),
    # path("user/registration",UserRegistrationView.as_view(),name="user_registration"),
    # path("mechanic/registration",MechanicRegistrationView.as_view(),name="mechanic_registration"),
    # path("carrental/registration",CarRenterRegistrationView.as_view(),name="car_registration"),
    path("add/profile/<int:pk>",MechanicProfileAddView.as_view(),name="add-profile"),
    path("profile/view/<int:pk>",MechanicProfileDetailView.as_view(),name="view-profile"),
    path('add/locations',AddLocationView.as_view(),name="add-locations"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
