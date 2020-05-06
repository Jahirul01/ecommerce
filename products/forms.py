from django import forms
from products.models import custommerOrder


class customerform(forms.ModelForm):
    class Meta:
        model = custommerOrder
        fields = "__all__"