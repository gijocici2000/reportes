# forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import Employee, Role, Report, ReportDetail


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    role = forms.ModelChoiceField(
        queryset=Role.objects.exclude(name__iexact='admin'),
        empty_label='Select Role'
    )

    code = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
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
                role=self.cleaned_data['role'],
                code=self.cleaned_data['code']
            )

        return user
    





# =========================
# REPORT FORM
# =========================

class ReportForm(forms.ModelForm):

    class Meta:

        model = Report

        fields = [
            'shift',
            'operator_code',
            'presentation',
            'machine',
            'state',
            'observation',
        ]

        widgets = {
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'operator_code': forms.Select(attrs={'class': 'form-control'}),
            'presentation': forms.Select(attrs={'class': 'form-control'}),
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Observaciones del turno'
            }),
        }

# =========================
# REPORT DETAIL FORM
# =========================

class ReportDetailForm(forms.ModelForm):

    class Meta:

        model = ReportDetail

        fields = [
            'box',
            'weight',
            'status',
            'observation',
        ]

        widgets = {

            'box': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),

            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),

            'observation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }