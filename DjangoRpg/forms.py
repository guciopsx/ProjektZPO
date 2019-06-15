from django import forms


class signup(forms.Form):
    email=forms.CharField(max_length=20)

