from django import forms

class Patients(forms.Form):
    name=forms.CharField(max_length=64)
    address=forms.CharField(max_length=64)
    age=forms.IntegerField()