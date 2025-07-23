from django.urls import path
from .views import ListaTareas, CrearTarea, EditarTarea, EliminarTarea

urlpatterns = [
    path('', ListaTareas.as_view(), name='lista_tareas'),
    path('crear/', CrearTarea.as_view(), name='crear_tarea'),
    path('editar/<int:pk>/', EditarTarea.as_view(), name='editar_tarea'),
    path('eliminar/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
]