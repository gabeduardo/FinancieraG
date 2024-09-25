from django.views.generic import ListView,DetailView, CreateView, DeleteView,UpdateView
from .models import Banco, Cliente, Credito 
from django.urls import reverse_lazy




""" Vistas para el manejo de las operaciones de los bancos  """
class BancoListView(ListView):
    model = Banco
    template_name = 'bancos/banco_list.html' 
    context_object_name = 'bancos'


class BancoDetailView(DetailView):
    model = Banco
    template_name = 'bancos/banco_detail.html' 
    context_object_name = 'banco'


class BancoCreateView(CreateView):
    model = Banco
    template_name = 'bancos/banco_form.html' 
    fields = ['nombre', 'tipo', 'direccion']
    
class BancoUpdateView(UpdateView):
    model = Banco
    template_name = 'bancos/banco_form.html' 
    fields = ['nombre', 'tipo', 'direccion']


class BancoDeleteView(DeleteView):
    model = Banco
    template_name = 'bancos/banco_confirm_delete.html' 
    success_url = reverse_lazy('members:bancos-list')  # Redirige a la lista de bancos después de eliminar el banco actual

""" fin de vistas para el  modelo banco  """



""" Vistas para el modelo  Cliente  """
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html' 
    context_object_name = 'clientes'
    
    
    

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html' 
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html' 
    fields = '__all__'
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html' 
    fields = '__all__'


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html' 
    success_url = reverse_lazy('members:cliente-list')  # Redirige a la lista de clientes
