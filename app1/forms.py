# library/forms.py

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'proveedor', 'fecha', 'cantidad', 'precio_unidad', 'precio_ganancias']
