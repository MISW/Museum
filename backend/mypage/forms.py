from django import forms
from django.http import request

from backend.users.models import User
from backend.models.models import DevelopmentInf

class ProfileUpdateForm(forms.ModelForm):
    generation = forms.IntegerField(required=False, max_value=999, min_value=0)
    description = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.FileField(required=False)

    class Meta:
        model = User
        fields = (
            'generation',
            'description',
            'image'
        )

class ApplicationCreateFrom(forms.ModelForm):
    title = forms.CharField(required=True, max_length=30)
    description = forms.CharField(required=False, widget=forms.Textarea)
    top_image = forms.FileField(required=False)
    is_public = forms.BooleanField(required=False)

    class Meta:
        model = DevelopmentInf
        fields = (
            'title',
            'description',
            'top_image',
            'is_public'
        )