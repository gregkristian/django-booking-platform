from django.urls import include, path

from .views import *

app_name = "booking"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("favorite/", favorite, name="favorite"),
    path("search/", SearchView.as_view(), name="search"),
    path(
        "employer/dashboard/",
        include(
            [
                path("", DashboardView.as_view(), name="employer-dashboard"),
                path("jobs/create/", BookableObjectCreateView.as_view(), name="employer-jobs-create"),
                path("jobs/<int:id>/edit/", JobUpdateView.as_view(), name="employer-jobs-edit"),
            ]
        ),
    ),
    path(
        "employee/",
        include(
            [
                path("favorites", FavoriteListView.as_view(), name="employee-favorites"),
            ]
        ),
    ),
    path("farms/", BookableObjectListView.as_view(), name="farms"),
    path("jobs/<int:id>/", JobDetailsView.as_view(), name="jobs-detail"),
]
