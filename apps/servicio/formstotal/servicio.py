from django import forms

from ..models import Servicio as Object, Persona


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
            # "proveedor":forms.CharField()
        }

    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name not in ("acabados", "inscrito_registro_publico", "tipo_inmueble", "prioridad"):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
            if field_name in ("proveedor"):
                self.fields[field_name].widget.attrs['style'] = "width: 100%"
                if field_name == "proveedor":
                    data = kwargs.get('data', None)
                    if data is None:
                        self.fields[field_name].queryset = Persona.objects.filter(id=0)
                    else:
                        self.fields[field_name].queryset = Persona.objects.filter(id=data['proveedor'])
            if field_name in ("tipo_inmueble", "prioridad"):
                self.fields[field_name].widget.attrs['class'] = 'form-control select2class'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
                self.fields[field_name].widget.attrs['style'] = "width: 100%"


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
            if field_name not in ("acabados", "inscrito_registro_publico", "tipo_inmueble", "prioridad"):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
            if field_name in ("proveedor", "cliente"):
                self.fields[field_name].widget.attrs['style'] = "width: 100%"
                if field_name == "proveedor":
                    data = kwargs.get('data', None)
                    objeto = kwargs['instance']
                    if data is None:
                        self.fields[field_name].queryset = Persona.objects.filter(id=objeto.proveedor.id)
                    else:
                        self.fields[field_name].queryset = Persona.objects.filter(id=data['proveedor'])
                if field_name == "cliente":
                    data = kwargs.get('data', None)
                    objeto = kwargs['instance']
                    if data is None:
                        self.fields[field_name].queryset = Persona.objects.filter(
                            id=objeto.cliente.id if objeto.cliente else 0)
                    else:
                        self.fields[field_name].queryset = Persona.objects.filter(
                            id=data['cliente'] if data['cliente'] else 0)

            if field_name in ("tipo_inmueble", "prioridad", "estado"):
                self.fields[field_name].widget.attrs['class'] = 'form-control select2class'
                self.fields[field_name].widget.attrs['autocomplete'] = "off"
                self.fields[field_name].widget.attrs['style'] = "width: 100%"
