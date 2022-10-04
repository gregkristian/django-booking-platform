from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from tags.models import Tag

from .manager import BookableEventManager

EVENT_TYPE = (("1", "Farm"), ("2", "Stuga"), ("3", "Other"))

class BookableEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #object = models.ForeignKey(Object) # TODO add
    event_name = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    num_bookings = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    objects = BookableEventManager()

    class Meta:
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse("jobs:jobs-detail", args=[self.id])

    def __str__(self):
        return self.event_name


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(BookableEvent, on_delete=models.CASCADE, related_name="applicants")
    created_at = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ["id"]
        unique_together = ["user", "job"]

    def __str__(self):
        return self.user.get_full_name()

    @property
    def get_status(self):
        if self.status == 1:
            return "Pending"
        elif self.status == 2:
            return "Accepted"
        else:
            return "Rejected"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(BookableEvent, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(default=timezone.now)
    soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.job.event_name
