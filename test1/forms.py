from django import forms

class UploadFileForm(forms.Form):
    folder = forms.CharField(max_length=1024)
    name   = forms.CharField(max_length=1024)
    file  = forms.FileField()

