from django import forms
from .models import Modal
from django.forms import ModelForm

class Modal(ModelForm):
    class Meta:
        model= Modal
        fields = ['__all__']