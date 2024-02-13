from PIL import Image
import datetime
from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import ModelProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class FormProfile(forms.ModelForm):
    class Meta:
        model = ModelProfile
        fields = ('image', 'bio', 'birth_date')

# # # # #
        
#Backup Form class
class FormLogin(AuthenticationForm):
    username = UsernameField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def confirm_login_allowed(self, user):
        if user.is_staff and not user.is_superuser:
            raise ValidationError(
                ("This account is not allowed here."),
                code='not_allowed',
            )


#Backup Form class
class FormSignup(UserCreationForm):
    
    username = forms.CharField(
        label=_('Username'),
        max_length=32,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(max_length=50, help_text='Valid e-mail is equired.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    
    password2 = forms.CharField(label=_('Repeat Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_('Enter the same password to confirm it.'))
    

    first_name = forms.CharField(max_length=60, min_length=4, required=False, help_text='Optional',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    
    last_name = forms.CharField(max_length=60, min_length=4, required=False, help_text='Optional',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}))
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]
    

    