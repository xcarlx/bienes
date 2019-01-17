from django import forms

from ..models import Principal as Object


class PrincipalForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"
        widgets = {
            "descripcion": forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(PrincipalForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name not in ("estado","imagen"):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
