from django import forms

class uploadData(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={"accept":"application/json"}))