from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

User = get_user_model()


class ProfileForm(UserChangeForm):
    first_name = forms.CharField(label=("Nombre"))
    last_name = forms.CharField(label="Apellido")
    birth_date = forms.DateField(label=("Fecha de nacimiento"), help_text='DD/MM/YYYY')
    location = forms.CharField(label=("País"), required=False)
    date_joined = forms.DateField(label=('Miembro desde:'), disabled=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'location', 'date_joined']
