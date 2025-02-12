from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="repo", max_length=100)