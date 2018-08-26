from django import forms
from django.forms import ModelForm, Textarea

from .models import Application

class ApplicationForm(forms.ModelForm):
    First_Name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control inlined", "placeholder":"What is your first name?"}))
    Last_Name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"What is your last name?"}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"What is your email address?"}))
    class Meta:
        model = Application
        fields = '__all__'