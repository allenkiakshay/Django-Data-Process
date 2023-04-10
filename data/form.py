from django import forms

from .models import Input


class ImageForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ("text","image")