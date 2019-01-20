from django import forms

from ..models import Servicio as Object


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = (
            'nombre', 'tipo_inmueble', 'proveedor', 'prioridad', 'descripcion', 'proyeccion', 'acabados',
            'inscrito_registro_publico', 'monto_venta')
        widgets = {
            "descripcion": forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            "proyeccion": forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name not in ("acabados", "inscrito_registro_publico"):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
