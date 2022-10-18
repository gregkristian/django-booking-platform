from django.urls import include, path

from .views import *

app_name = "booking"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("favorite/", favorite, name="favorite"),
    path("search/", SearchView.as_view(), name="search"),
    path(
        "owner/dashboard/",
        include(
            [
                path("", DashboardView.as_view(), name="owner-dashboard"),
                path("create/", BookableObjectCreateView.as_view(), name="create-object"),
                path("edit/<int:id>/", BookableObjectEditView.as_view(), name="edit-object"),
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
