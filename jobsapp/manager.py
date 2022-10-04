from django.db import models

class BookableEventManager(models.Manager):
    # Placeholder class for manager. Example below

    def with_description(self, *args, **kwargs):
        return self.filter(description!="", *args, **kwargs)
    