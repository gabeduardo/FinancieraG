from django.views.generic import ListView,DetailView, CreateView, DeleteView,UpdateView
from .models import Banco, Cliente, Credito 
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from .forms import ClienteForm

""" Vistas para el manejo de las operaciones de los bancos  """
class BancoListView(ListView):
    """
        Vista  de tipo ListView para listar los bancos .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
    """
    model = Banco
    template_name = 'bancos/banco_list.html' 
    context_object_name = 'bancos'


class BancoDetailView(DetailView):
    """
        Vista  de tipo DetailView que muestra el detalle de un banco en especifico .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
    """
    model = Banco
    template_name = 'bancos/banco_detail.html' 
    context_object_name = 'banco'


class BancoCreateView(CreateView):
    """
        Vista  de tipo CreateView usada para crear los bancos .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
        - success_url: url a la cual se redirige despues de ser ejecutada correctamente
    """
    model = Banco
    template_name = 'bancos/banco_form.html' 
    fields = ['nombre', 'tipo', 'direccion']
    success_url = reverse_lazy('members:bancos-list') 
    def form_valid(self, form):
        # Codigo apra mandar mensaje de exito al usuario de la accion realizada
        messages.success(self.request, '¡El banco se creó exitosamente!')
        return super().form_valid(form)
    
class BancoUpdateView(UpdateView):
    """
        Vista  de tipo CreateView usada para crear los bancos .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
        - success_url: url a la cual se redirige despues de ser ejecutada correctamente
    """
    model = Banco
    template_name = 'bancos/banco_form.html' 
    fields = ['nombre', 'tipo', 'direccion']
    success_url = reverse_lazy('members:bancos-list') 
    
    def form_valid(self, form):
        """ Codigo apra poder mandar mensaje de exito al usuario de la accion realizada """
        messages.success(self.request, '¡El banco se actualizó exitosamente!')
        return super().form_valid(form)
    
class BancoDeleteView(DeleteView):
    """
        Vista  de tipo DeleteView usada para eliminar un banco .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - template_name: Nombre de la plantilla que se va a  renderizar
        - success_url: url a la cual se redirige despues de ser ejecutada correctamente
    """
    model = Banco
    template_name = 'bancos/banco_confirm_delete.html' 
    success_url = reverse_lazy('members:bancos-list')  # Redirige a la lista de bancos después de eliminar el banco actual

    def form_valid(self, form):
        """ metodo apra mandar mensaje de elimiancion correcta """
        obj = self.get_object()
        messages.success(self.request, f' Banco {obj} eliminado correctamente')
        return super().form_valid(form)
""" fin de vistas para el  modelo banco  """



""" Vistas para el modelo  Cliente  """
class ClienteListView(ListView):
    """
        Vista  de tipo ListView para listar los bancos .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
        - success_url: url a la cual se redirige despues de ser ejecutada correctamente
    """
    model = Cliente
    template_name = 'clientes/cliente_list.html' 
    context_object_name = 'clientes'
    success_url = reverse_lazy('members:cliente-list') 
    
    
    

class ClienteDetailView(DetailView):
    """
        Vista  de tipo DetailView que muestra el detalle de un cliente en especifico .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
    """
    model = Cliente
    template_name = 'clientes/cliente_detail.html' 
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    """
        Vista  de tipo CreateView usada para crear los bancos .
        posee parámetros:
        
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
        - success_url: url a la cual se redirige despues de ser ejecutada correctamente
        - form_class: formulario utilizado a la hora de crear un cliente, se encuentra definido en forms.py y agrega widgets para el template
    """
    model = Cliente
    template_name = 'clientes/cliente_form.html' 
    success_url = reverse_lazy('members:cliente-list') 
    
    form_class = ClienteForm
    
    def form_valid(self, form):
        """ Codigo apra mandar mensaje de exito al usuario de la accion realizada """
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
    """
        Vista  de tipo CreateView usada para crear los creditos .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - fields : para especificar que campos se van a mostrar en el formulario
        - template_name: Nombre de la plantilla que se va a  renderizar
        - success_url: url a la cual se redirige despues de ser ejecutada correctamente
    """
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
    """
        Vista  de tipo ListView para listar los bancos .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
       
    """
    model = Credito
    template_name = 'creditos/credito_list.html' 
    context_object_name = 'creditos'
    
    
class CreditoDetailView(DetailView):
    """
        Vista  de tipo DetailView que muestra el detalle de un credito en especifico .
        posee parámetros:
        - model: modelo utilizado para crear la class based view 
        - context_object_name: Nombre del objeto de contexto para la plantilla
        - template_name: Nombre de la plantilla que se va a  renderizar
    """
    model = Credito
    template_name = 'creditos/credito_detail.html' 
    context_object_name = 'credito'