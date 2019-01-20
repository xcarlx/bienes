from django import forms


class TipoServicioForm(forms.Form):
    TIPO_INMUEBLE = (
        ('TE', 'Terreno'),
        ('DE', 'Departamento'),
        ('CA', 'Casa')
    )
    tipo_inmueble = forms.ChoiceField(choices=TIPO_INMUEBLE)

    def __init__(self, *args, **kwargs):
        super(TipoServicioForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name not in ("estado", "imagen"):
                self.fields[field_name].widget.attrs['class'] = 'form-control font-combo-16'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
