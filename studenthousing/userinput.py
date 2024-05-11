from django import forms
import json
from .models import UserQuery

class MyForm(forms.Form):
    name = forms.CharField(label='User search criteria', max_length=500)

