from django import forms
from .models import Articulo

class FormArticulo(forms.ModelForm):

    #campos del modelo
    class Meta:
        model = Articulo
        fields = ('seccion', 'fecha_publicacion', 'titulo', 'contenido', 'imagen','precio')
        widgets = {
            'fecha_publicacion': forms.SelectDateWidget(attrs={'class': 'pub_fecha_publicacion'}),
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'contenido': forms.Textarea(attrs={'class': 'pub_contenido'}),
            'precio': forms.NumberInput(attrs={'class': 'pub_precio'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'pub_imagen'}),
        }