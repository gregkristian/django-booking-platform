from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView

from accounts.forms import VisitorProfileUpdateForm
from accounts.models import User
from bookingapp.decorators import user_is_visitor
from bookingapp.models import Favorite

class VisitorEditProfileView(UpdateView):
    model = User
    form_class = VisitorProfileUpdateForm
    context_object_name = "employee"
    template_name = "accounts/visitor-edit-profile.html"
    success_url = reverse_lazy("accounts:visitor-profile-update")

    @method_decorator(login_required(login_url=reverse_lazy("accounts:login")))
    @method_decorator(user_is_visitor)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj


@method_decorator(login_required(login_url=reverse_lazy("accounts:login")), name="dispatch")
@method_decorator(user_is_visitor, name="dispatch")
class FavoriteListView(ListView):
    model = Favorite
    template_name = "jobs/employee/favorites.html"
    context_object_name = "favorites"

    def get_queryset(self):
        return self.model.objects.select_related("job__user").filter(soft_deleted=False, user=self.request.user)
