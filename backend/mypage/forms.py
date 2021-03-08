from django import forms

from backend.developments.models import (
    Development,
    Media,
    Link,
    ASSOCIATION_CHOICES,
    MEDIA_CHOICES,
    LINK_CHOICES
)
from backend.users.models import User


class ProfileUpdateForm(forms.ModelForm):
    generation = forms.IntegerField(required=False, max_value=999, min_value=0)
    associations = forms.MultipleChoiceField(
        choices=ASSOCIATION_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    description = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.FileField(required=False)


    class Meta:
        model = User
        fields = (
            'generation',
            'description',
            'image'
        )


class DevelopmentCreateForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=30)
    description = forms.CharField(required=False, widget=forms.Textarea)
    co_developers = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    associations = forms.MultipleChoiceField(
        choices=ASSOCIATION_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    top_image = forms.FileField(required=False)
    is_private = forms.BooleanField(required=False)

    class Meta:
        model = Development
        fields = (
            'title',
            'description',
            'top_image',
            'is_private'
        )


class MediaCreateForm(forms.ModelForm):
    MEDIA_CHOICES_WITH_EMPTY = [(None, '----')] + list(MEDIA_CHOICES)

    # link form とのid衝突回避のため
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES_WITH_EMPTY, label='type', required=False)
    file = forms.FileField(required=False)

    class Meta:
        model = Media
        fields = (
            'media_type',
            'file'
        )

class LinkCreateForm(forms.ModelForm):
    LINK_CHOICES_WITH_EMPTY = [(None, '----')] + list(LINK_CHOICES)

    # media form とのid衝突回避のため
    link_type = forms.ChoiceField(choices=LINK_CHOICES_WITH_EMPTY, label='type', required=False)
    link = forms.URLField(required=False)

    class Meta:
        model = Link
        fields = (
            'link_type',
            'link'
        )

class DevelopmentUpdateForm(DevelopmentCreateForm):
    title = forms.CharField(required=False, max_length=30)

    class Meta:
        model = Development
        fields = (
            'title',
            'description',
            'top_image',
            'is_private'
        )