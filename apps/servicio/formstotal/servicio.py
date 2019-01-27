from django import forms

from ..models import Servicio as Object


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = (
            'nombre', 'tipo_inmueble', 'proveedor', 'prioridad', 'ciudad', 'lugar', 'direccion', 'referencia',
            'descripcion', 'proyeccion', 'acabados', 'inscrito_registro_publico', 'monto_soles', 'monto_dolares',
            'metros_cuadrados')
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


class ServicioEditarForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = (
            'nombre', 'tipo_inmueble', 'proveedor', 'prioridad', 'ciudad', 'lugar', 'direccion', 'referencia',
            'descripcion', 'proyeccion', 'acabados', 'inscrito_registro_publico', 'monto_soles', 'monto_dolares',
            'cliente', 'estado', 'monto_vendido'
        )
        widgets = {
            "descripcion": forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            "proyeccion": forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(ServicioEditarForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name not in ("acabados", "inscrito_registro_publico"):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
