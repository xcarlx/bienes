from django import forms

from ..models import Video as Object


class VideoForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['autocomplete'] = "off"
        self.fields['servicio'].widget = forms.HiddenInput()
