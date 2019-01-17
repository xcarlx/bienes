from django import forms
from django.contrib.auth.forms import AuthenticationForm


# AuthenticationForm.fields['password']
# AuthenticationForm.fields['username']

class FormLogin(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = "form-control"
        self.fields['password'].widget.attrs["class"] = "form-control"
