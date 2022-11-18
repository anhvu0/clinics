from django import forms
import random

class Search(forms.Form):
    name=forms.CharField(label="Enter the patient's name")

class Add(forms.Form):
    name=forms.CharField(label="name")
    Age=forms.IntegerField(label="age")
    Address=forms.CharField(label="address")
    Id=forms.IntegerField(label="id")