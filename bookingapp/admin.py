from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

# Register your models here.
from bookingapp.models import BookableObject

@admin.register(BookableObject)
class BookableObjectAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "type",
        "owner",
        "address",
        "latitude",
        "longitude",
        "description",
        "creation_date",
    ]
    list_filter = ["owner", "type"]
    date_hierarchy = "creation_date"
