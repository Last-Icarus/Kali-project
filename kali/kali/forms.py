from django import forms
from .models import UserSettings, Art, ArtImage, ArtTag
from django.forms import formset_factory

class ImageForm(forms.ModelForm):

    class Meta:
        model = UserSettings
        exclude = ('user',)

class ArtForm(forms.ModelForm):

    class Meta:
        model = ArtImage
        exclude = ('art',)
        labels = {
            'image' : ''
        }

ArtFormSet = formset_factory(ArtForm, max_num=5, extra=5)
