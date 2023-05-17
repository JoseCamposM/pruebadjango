from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('expedientes', views.expedientes, name='expedientes'),
    path('expedientes/crearExp', views.crearExpediente, name='crear'),
    path('expedientes/editarExp', views.editarExpediente, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('expedientes/editar/<int:id>', views.editarExpediente, name='editar'),

]