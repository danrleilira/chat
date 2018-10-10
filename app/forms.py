from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name")
        field_classes = {'username': UsernameField}
