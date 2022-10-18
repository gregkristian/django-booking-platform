from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from ..decorators import user_is_employee
from ..models import Favorite, BookableObject


class HomeView(ListView):
    model = BookableObject
    template_name = "home.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchView(ListView):
    model = BookableObject
    template_name = "jobs/search.html"
    context_object_name = "jobs"

    def get_queryset(self):
        # q = JobDocument.search().query("match", title=self.request.GET['position']).to_queryset()
        # print(q)
        # return q
        return self.model.objects.filter(
            location__contains=self.request.GET.get("location", ""),
            title__contains=self.request.GET.get("position", ""),
        )


class BookableObjectListView(ListView):
    model = BookableObject
    template_name = "listing/listing.html"
    context_object_name = "listing"
    paginate_by = 5


class JobDetailsView(DetailView):
    model = BookableObject
    template_name = "jobs/details.html"
    context_object_name = "job"
    pk_url_kwarg = "id"

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # raise error
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def favorite(request):
    if not request.user.is_authenticated:
        return JsonResponse(data={"auth": False, "status": "error"})

    job_id = request.POST.get("job_id")
    user_id = request.user.id
    try:
        fav = Favorite.objects.get(job_id=job_id, user_id=user_id, soft_deleted=False)
        if fav:
            fav.soft_deleted = True
            fav.save()
            return JsonResponse(
                data={"auth": True, "status": "removed", "message": "Job removed from your favorite list"}
            )
    except Favorite.DoesNotExist:
        Favorite.objects.create(job_id=job_id, user_id=user_id)
        return JsonResponse(data={"auth": True, "status": "added", "message": "Job added to your favorite list"})
