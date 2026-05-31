# forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Employee, Role


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    role = forms.ModelChoiceField(
        queryset=Role.objects.exclude(name__iexact='admin'),
        empty_label='Select Role'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'role'
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:

            user.save()

            Employee.objects.create(
                user=user,
                role=self.cleaned_data['role']
            )

        return user