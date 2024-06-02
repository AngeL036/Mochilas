from django.urls import path
from .views import IndexView,AgregarView,nuevo_producto,listar_productos

urlpatterns = [
    path('',IndexView,name='indexView'),
    path('AgregarView/',AgregarView,name='AgregarView' ),
    path('nuevo_producto/',nuevo_producto,name='nuevo_producto'),
    path('listar_productos/',listar_productos,name='listar_productos')
]