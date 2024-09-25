from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.urls import reverse
class Banco(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=[("Privado", "Privado"), ("Gobierno", "Gobierno")])
    direccion = models.TextField()

    def __str__(self):
        return self.nombre
    
    # url absoluta para el banco y que funciona ademas apra redirigir 
    def get_absolute_url(self):
        
        return reverse('members:banco-detail', args=[str(self.id)])

class Cliente(models.Model):
    nombre_apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="La edad debe ser mayor o igual a 1."),
            MaxValueValidator(99, message="La edad debe ser menor o igual a 99.")
        ],
        blank=True,
        null=True
    )
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    direccion_habitacion = models.TextField(blank=True, null=True)
    correo_electronico = models.CharField(
        max_length=100,
        validators=[EmailValidator(message="Ingresa un correo electrónico válido.")]
    )
    telefono = models.CharField(max_length=20, blank=True, null=True)
    TIPO_PERSONA_CHOICES = [("Natural", "Natural"), ("Jurídico", "Jurídico")]
    tipo_persona = models.CharField(max_length=20, choices=TIPO_PERSONA_CHOICES, blank=True, null=True)
    banco_cuenta = models.ForeignKey(Banco, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre_apellido
    
        # url absoluta para el cliente y que funciona ademas apra redirigir 
    def get_absolute_url(self):
        
        return reverse('members:cliente-detail', args=[str(self.id)])

class Credito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion_credito = models.TextField()
    pago_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    pago_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    plazo_meses = models.PositiveIntegerField()
    fecha_registro = models.DateField(auto_now_add=True, blank=True, null=True)
    banco_otorgante = models.ForeignKey(Banco, on_delete=models.CASCADE)
    TIPO_CREDITO_CHOICES = [("Automotriz", "Automotriz"), ("Hipotecario", "Hipotecario"), ("Comercial", "Comercial")]
    tipo_credito = models.CharField(max_length=20, choices=TIPO_CREDITO_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Credito para {self.cliente.nombre_apellido}"
    
    def get_absolute_url(self):
        
        return reverse('members:credito-detail', args=[str(self.id)])

