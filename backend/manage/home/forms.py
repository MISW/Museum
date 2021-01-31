from django import forms

from backend.developments.models import Development, STATUS_CHOICES


class StatusUpdateForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)

    class Meta:
        model = Development
        fields = (
            'status',
        )
