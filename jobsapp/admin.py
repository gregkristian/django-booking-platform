from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

# Register your models here.
from jobsapp.models import BookableEvent


@admin.register(BookableEvent)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "event_name",
        "address",
        "latitude",
        "longitude",
        "description",
        "created_at",
        "num_bookings",
        "user",
    ]
    list_filter = ["created_at", "user"]
    date_hierarchy = "created_at"
