from django import forms
from .models import Post, Profile


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class ProfileForm(forms.ModelForm):
    '''
    classs that creates profile update form
    '''
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']


class PostForm(forms.ModelForm):
    '''
    classs that creates profile update form
    '''
    class Meta:
        model = Post
        fields = ['title', 'landing_image', 'site_link']


class CountryForm(forms.Form):
    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)
