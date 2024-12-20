from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserSpace, StoredContent
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

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
        
        

class UserProfileCreationForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    photo = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        # Create or update the profile
        profile = UserProfile.objects.create(user=user, bio=self.cleaned_data['bio'], photo=self.cleaned_data.get('photo'))
        return user

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'bio']  
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}), 
        }
