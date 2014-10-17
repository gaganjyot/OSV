# -*- coding: utf-8 -*-
from django import forms

class login_form(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label ="password", max_length=20, widget=forms.PasswordInput)

class register_form(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label ="password", max_length=20, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=40)

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file', help_text='max. 42 megabytes' )

class loc_form(forms.Form):
    docfile = forms.CharField(widget=forms.HiddenInput)
    loc_x = forms.FloatField(widget=forms.HiddenInput)
    loc_y = forms.FloatField(widget=forms.HiddenInput)
