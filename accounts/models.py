from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_bibliotecario = models.BooleanField(default=False)
    is_socio = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set', # Modificado para evitar conflictos con el related_name del modelo User que ya tiene django
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Carnet(models.Model):
    numero = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/')
    foto = models.ImageField(upload_to='fotos_socios/')
    fecha_emision = models.DateField(auto_now_add=True)
    fecha_expiracion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Carnet {self.numero}"

class Direccion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=[('Residencial', 'Residencial'), ('Laboral', 'Laboral')])

    def __str__(self):
        return f"{self.tipo}: {self.direccion}"

class Telefono(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='telefonos')
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50, choices=[('Movil', 'Movil'), ('Fijo', 'Fijo')])

    def __str__(self):
        return f"{self.tipo}: {self.telefono}"

class Socio(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='socio_profile')
    carnet = models.OneToOneField(Carnet, on_delete=models.CASCADE, related_name='socio_carnet')
    fecha_nacimiento = models.DateField()
    estudiante = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.carnet.numero}"

class Bibliotecario(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='bibliotecario_profile')
    empleado_id = models.CharField(max_length=20, unique=True)
    carnet = models.OneToOneField(Carnet, on_delete=models.CASCADE, related_name='bibliotecario_carnet')
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.empleado_id}"
