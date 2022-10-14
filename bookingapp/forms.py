from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from bookingapp.models import Applicant, BookableObject


class CreateBookableObjectForm(forms.ModelForm):
    class Meta:
        model = BookableObject
        exclude = ('owner','creation_date')

    def is_valid(self):
        valid = super(CreateBookableObjectForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def clean_tags(self):
        tags = self.cleaned_data["tags"]
        if len(tags) > 6:
            raise forms.ValidationError("You can't add more than 6 tags")
        return tags

    def save(self, commit=True):
        job = super(CreateBookableObjectForm, self).save(commit=False)
        if commit:
            job.save()
            for tag in self.cleaned_data["tags"]:
                job.tags.add(tag)
        return job


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ("job",)
