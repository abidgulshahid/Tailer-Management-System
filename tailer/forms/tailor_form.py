from django.contrib.auth.models import User
from django import forms
from tailer.models import Customer
import re


class TailorForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TailorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            self.fields[field].required = False
        self.fields['order_take'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['order_take'].widget.attrs['class'] = "form-control"

        self.fields['order_deadline'].widget = forms.TextInput(attrs={'type': 'date'})
        self.fields['order_deadline'].widget.attrs['class'] = "form-control"

        self.fields['name'].required = True
        self.fields['phone_number'].required = True

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        number_pattern = re.compile(r'\d+')
        if number_pattern.findall(phone_number):
            return  phone_number
        raise forms.ValidationError("Only Numbers are allowed")

    def clean_length(self):
        id_length = self.cleaned_data['length']
        number_pattern = re.compile(r'\d+')
        if id_length and number_pattern.findall(id_length):
            return id_length
        raise forms.ValidationError("Only Numbers are allowed")


