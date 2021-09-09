from django import forms
from django.db.models.fields import CharField, TextField
from django.forms import ModelForm
from . models import Personal_Details
from phonenumber_field.widgets import PhoneNumberPrefixWidget
class DateInp(forms.DateInput):
    input_type = "date"


class Personal_details(ModelForm):
    class Meta:
        gender_choice = [
        (1,'Male'),('Female','Female'),('Other','Other')
        ]
        model = Personal_Details
        fields = '__all__'
        widgets = {
            'mobile': PhoneNumberPrefixWidget(initial = "IN",attrs={'class':'form-control'}),
            'dob':DateInp(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control'}),
            "institute_address":forms.Textarea(attrs={'rows':'4'}),
            'gender':forms.RadioSelect(choices=gender_choice,attrs={'id':'gender','class':'gender'}),
            'password': forms.PasswordInput(attrs={'id':"password"})

        }