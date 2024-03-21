from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Admin URLs
path("admin/home", AdminHomeView.as_view(), name="admin-home"),
path("register/admin", AdminRegistrationView.as_view(), name="admin-registration"),
path('login/admin', AdminLoginView.as_view(), name='admin-login'),
path('add/locations', AddLocationView.as_view(), name="add-locations"),
path('approval/<int:pk>', approve_mechanic, name="approve"),

# Mechanic URLs
path("mechanic/home", MechnaicHomeView.as_view(), name="mechanic_home"),
path("add/profile/<int:pk>", MechanicProfileAddView.as_view(), name="add-profile"),
path("profile/view/<int:pk>", MechanicProfileDetailView.as_view(), name="view-profile"),
path("profile/update/<int:pk>", MechanicprofileUpdateView.as_view(), name="update-profile"),
path('pending', PendingMechanicView.as_view(), name="pending-list"),
path('my-requests/', MechanicReqListView.as_view(), name='mechanic_requests'),
path('mechanicapproval/<int:pk>', update_status, name="mech-approve"),
path('feedback-list/', FeedbackListView.as_view(), name='feedback_list'),
path('create-bill-payment/<int:pk>/', BillPaymentCreateView.as_view(), name='create_bill_payment'),



# User URLs
path("user/home", UserHomeView.as_view(), name="user_home"),
path("user/registration", RegistrationView.as_view(), name="user_registration"),
path("useradd/profile/<int:pk>", UserProfileAddView.as_view(), name="useradd-profile"),
path("userprofile/view/<int:pk>", UserProfileDetailView.as_view(), name="userview-profile"),
path("userprofile/update/<int:pk>", UserProfileUpdateView.as_view(), name="userupdate-profile"),
path('approved-mechanics/', ApprovedMechanicListView.as_view(), name='approved_mechanics'),
path("create/req/<int:mechanic_id>", ReqToMechanicCreateView.as_view(), name="create_req"),
path('requests/', UserRequestsListView.as_view(), name='user_requests'),
path('feedback/<int:pk>', FeedBackCreateView.as_view(), name='feedback_form'),
path('bill-payment/<int:pk>/', bil_payment, name='bill_payment'),

# Common URLs
path("",HomeView.as_view(),name="home"),
path('login/', LoginView.as_view(), name='login'),
path('logout/', LogoutView, name='logout'), 
path("payment/sucess/",PaymentSuccessView.as_view(),name="payment"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
