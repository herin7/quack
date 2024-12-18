from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserSpace, StoredContent

class CustomURLForm(forms.ModelForm):
    custom_url = forms.SlugField(
        help_text="Choose a unique URL for your personal space",
        max_length=50,
        required=True
    )

    class Meta:
        model = UserSpace
        fields = ['custom_url']

class StoredContentForm(forms.ModelForm):
    class Meta:
        model = StoredContent
        fields = ['title', 'content_type', 'text_content', 'file_content']
        widgets = {
            'content_type': forms.Select(attrs={'id': 'content-type-select'}),
        }