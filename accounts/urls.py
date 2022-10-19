from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from bookingapp.views import EditProfileView, EmployerProfileEditView

from .views import *

app_name = "accounts"

urlpatterns = [
    path("visitor/register/", VisitorRegistrationView.as_view(), name="visitor-register"),
    path("owner/register/", OwnerRegistrationView.as_view(), name="owner-register"),
    path("employee/profile/update/", EditProfileView.as_view(), name="employee-profile-update"),
    path("employer/profile/update/", EmployerProfileEditView.as_view(), name="employer-profile-update"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
