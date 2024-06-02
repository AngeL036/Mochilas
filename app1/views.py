from django.shortcuts import render,redirect
from .forms import ProductoForm
from .models import Producto
# Create your views here.
def IndexView(request):
    return render(request,'index.html')

def AgregarView(request):
    return render(request,'agregar.html')

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexView')
    else:
        form = ProductoForm()
    return render(request,'Agregar.html',{'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mostrar.html',{'productos': productos})
