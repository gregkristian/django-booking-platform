from collections import namedtuple
from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from tags.models import Tag

from .manager import BookableObjectManager

OBJECT_TYPE = (("1", "Farm"), ("2", "Stuga"), ("3", "Other"))

class BookableObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=OBJECT_TYPE, max_length=10)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)

    objects = BookableObjectManager()

    class Meta:
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse("jobs:jobs-detail", args=[self.id])

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(BookableObject, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(default=timezone.now)
    soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.job.event_name
