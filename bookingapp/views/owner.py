from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from accounts.forms import OwnerProfileUpdateForm
from bookingapp.decorators import user_is_employer
from bookingapp.forms import CreateBookableObjectForm
from bookingapp.models import BookableObject
from tags.models import Tag


class DashboardView(ListView):
    model = BookableObject
    template_name = "jobs/employer/dashboard.html"
    context_object_name = "jobs"

    @method_decorator(login_required(login_url=reverse_lazy("accounts:login")))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(owner_id=self.request.user.id)

class BookableObjectCreateView(CreateView):
    template_name = "listing/create.html"
    form_class = CreateBookableObjectForm
    extra_context = {"title": "Post New Listing"}
    success_url = reverse_lazy("booking:owner-dashboard")

    @method_decorator(login_required(login_url=reverse_lazy("accounts:login")))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy("accounts:login")
        if self.request.user.is_authenticated and self.request.user.role != "employer":
            return reverse_lazy("accounts:login")
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookableObjectCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@method_decorator(login_required(login_url=reverse_lazy("accounts:login")), name="dispatch")
@method_decorator(user_is_employer, name="dispatch")
class BookableObjectEditView(UpdateView):
    template_name = "listing/edit.html"
    form_class = CreateBookableObjectForm
    extra_context = {"title": "Edit Listing"}
    slug_field = "id"
    slug_url_kwarg = "id"
    success_url = reverse_lazy("booking:owner-dashboard")

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return BookableObject.objects.filter(owner=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Job updated successfully")
        return super(BookableObjectEditView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class OwnerProfileEditView(UpdateView):
    form_class = OwnerProfileUpdateForm
    context_object_name = "employer"
    template_name = "accounts/owner-edit-profile.html"
    success_url = reverse_lazy("accounts:owner-profile-update")

    @method_decorator(login_required(login_url=reverse_lazy("accounts:login")))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj
