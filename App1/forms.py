from django import forms
from django.db.models.fields import CharField, TextField
from django.forms import ModelForm
from django.forms.fields import FileField
from . models import Personal_Details
from phonenumber_field.widgets import PhoneNumberPrefixWidget
class DateInp(forms.DateInput):
    input_type = "date"


class Personal_details(ModelForm):
    class Meta:
        gender_choice = [('Male','Male'),('Female','Female'),('Other','Other'),]
        relationship_choice = [('married','Married'),('unmarried','Unmarried')]
        model = Personal_Details
        fields = '__all__'
        widgets = {
            
            'dob':DateInp(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control'}),
            "institute_address":forms.Textarea(attrs={'rows':'4'}),
            'gender':forms.RadioSelect(choices=gender_choice,attrs={'id':'gender','class':'gender'}),
            'relationship_status':forms.RadioSelect(choices=relationship_choice,attrs={'id':'relationship_status','class':'relationship_status'}),
            'password': forms.PasswordInput(attrs={'id':"password"}),
            'upload_resume': forms.FileInput(attrs={'id':'resume','accept':"application/pdf, application/vnd.ms-excel"}),
            'profile_pic': forms.FileInput(attrs={'id':'profile_pic', 'accept':"image/*"})
        }
    