from django import forms
from ..models import Comentario as Object


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"
        widgets = {
            "texto": forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['autocomplete'] = "off"

        self.fields['servicio'].widget = forms.HiddenInput()
