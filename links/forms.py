from django.forms import ModelForm, BooleanField

from links.models import Link


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class LinkForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Link
        fields = ('full_url', )
