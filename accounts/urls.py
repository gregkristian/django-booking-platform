from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from bookingapp.views import VisitorEditProfileView, OwnerProfileEditView

from .views import *

app_name = "accounts"

urlpatterns = [
    path("visitor/register/", VisitorRegistrationView.as_view(), name="visitor-register"),
    path("owner/register/", OwnerRegistrationView.as_view(), name="owner-register"),
    path("visitor/profile/update/", VisitorEditProfileView.as_view(), name="visitor-profile-update"),
    path("owner/profile/update/", OwnerProfileEditView.as_view(), name="owner-profile-update"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
