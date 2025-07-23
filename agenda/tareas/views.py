from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarea

class ListaTareas(ListView):
    model = Tarea
    template_name = 'tareas/lista.html'

class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('lista_tareas')
    template_name = 'tareas/formulario.html'

class EditarTarea(UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('lista_tareas')
    template_name = 'tareas/formulario.html'

class EliminarTarea(DeleteView):
    model = Tarea
    success_url = reverse_lazy('lista_tareas')
    template_name = 'tareas/confirmar_eliminacion.html'

# Create your views here.
