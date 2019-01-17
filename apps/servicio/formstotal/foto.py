from django import forms
from ..models import Foto as Object


class FotoForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FotoForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name not in ('imagen',):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
        self.fields['servicio'].widget = forms.HiddenInput()
