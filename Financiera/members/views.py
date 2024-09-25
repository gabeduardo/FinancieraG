from django.views.generic import ListView,DetailView, CreateView, DeleteView,UpdateView
from .models import Banco, Cliente, Credito 
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from .forms import ClienteForm

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
    success_url = reverse_lazy('members:bancos-list') 
    def form_valid(self, form):
        # Codigo apra mandar mensaje de exito al usuario de la accion realizada
        messages.success(self.request, '¡El banco se creó exitosamente!')
        return super().form_valid(form)
    
class BancoUpdateView(UpdateView):
    model = Banco
    template_name = 'bancos/banco_form.html' 
    fields = ['nombre', 'tipo', 'direccion']
    success_url = reverse_lazy('members:bancos-list') 
    def form_valid(self, form):
        # Codigo apra mandar mensaje de exito al usuario de la accion realizada
        messages.success(self.request, '¡El banco se actualizó exitosamente!')
        return super().form_valid(form)
    
class BancoDeleteView(DeleteView):
    model = Banco
    template_name = 'bancos/banco_confirm_delete.html' 
    success_url = reverse_lazy('members:bancos-list')  # Redirige a la lista de bancos después de eliminar el banco actual

    def form_valid(self, form):
        # metodo apra mandar mensaje de elimiancion correcta
        obj = self.get_object()
        messages.success(self.request, f' Banco {obj} eliminado correctamente')
        return super().form_valid(form)
""" fin de vistas para el  modelo banco  """



""" Vistas para el modelo  Cliente  """
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html' 
    context_object_name = 'clientes'
    success_url = reverse_lazy('members:cliente-list') 
    
    
    

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html' 
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html' 
    success_url = reverse_lazy('members:cliente-list') 
    
    form_class = ClienteForm
    
    def form_valid(self, form):
        # Codigo apra mandar mensaje de exito al usuario de la accion realizada
        messages.success(self.request, '¡El cliente se creó exitosamente!')
        return super().form_valid(form)
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html' 
    fields = '__all__'
    success_url = reverse_lazy('members:cliente-list') 
    
    def form_valid(self, form):
        # Codigo apra mandar mensaje de exito al usuario de la accion realizada
        messages.success(self.request, '¡El cliente se actualizó exitosamente!')
        return super().form_valid(form)


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html' 
    success_url = reverse_lazy('members:cliente-list')  # Redirige a la lista de clientes
    
    def form_valid(self, form):
        # metodo apra mandar mensaje de elimiancion correcta
        obj = self.get_object()
        messages.success(self.request, f' Cliente {obj} eliminado correctamente')
        return super().form_valid(form)

""" 
find e vistas apra el cliente  """




""" inicio de las vistas para el manejo de creditos  """

class CreditoCreateView(CreateView):
    model = Credito
    template_name = 'creditos/credito_form.html' 
    fields = '__all__'
    success_url = reverse_lazy('members:credito-list') 
    
    def get_success_url(self):

        return reverse('members:credito-list')
    
    def form_valid(self, form):
        # Codigo apra mandar mensaje de exito al usuario de la accion realizada
        messages.success(self.request, '¡El crédito se creó exitosamente!')
        return super().form_valid(form)
    
    
class CreditoListView(ListView):
    model = Credito
    template_name = 'creditos/credito_list.html' 
    context_object_name = 'creditos'
    
    
class CreditoDetailView(DetailView):
    model = Credito
    template_name = 'creditos/credito_detail.html' 
    context_object_name = 'credito'