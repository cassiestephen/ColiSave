from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # allows u to create users
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms 

from .models import Client


# register user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] # password 2 confirms password 1


# login user
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# create a client (model), adds a horse
class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'owner', 'phone', 'address', 'city', 'state', 'country', 
                  'surgery', 'age',	'rectal_temp', 'pulse', 'respiratory_rate', 'temp_of_extremities', 'peripheral_pulse', 'mucous_membrane', 'capillary_refill_time',
                  'pain', 'peristalsis', 'abdominal_distention', 'packed_cell_volume', 'total_protein',
                  'surgical_lesion', 'lesion_1', 'lesion_2', ]
                #fields = #['first_name', 'last_name', 'phone', 'email', 'address', 'city', 'state', 'country']


# update a client (model), adds a horse
class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'owner', 'phone', 'address', 'city', 'state', 'country',
                  'surgery', 'age',	'rectal_temp', 'pulse', 'respiratory_rate', 'temp_of_extremities', 'peripheral_pulse', 'mucous_membrane', 'capillary_refill_time',
                   'pain', 'peristalsis', 'abdominal_distention', 'packed_cell_volume', 'total_protein',
                  'surgical_lesion', 'lesion_1', 'lesion_2', ]