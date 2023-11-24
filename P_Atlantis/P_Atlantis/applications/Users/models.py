from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from ..Pedido.models import pedido
class User(AbstractBaseUser, PermissionsMixin):
    usuario='U'
    administrador='A'
    choices_roles=(
        (usuario,'usuario'),
        (administrador,'administrador')
    )
    choices_genero=(

        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros')
    )

    username = models.CharField('usuario_table',unique=True,max_length=250)
    dni = models.CharField('dni', max_length=13,unique=True)
    email = models.EmailField('email', max_length=254)
    nombre = models.CharField('nombre',max_length=250)
    apellido_paterno = models.CharField('apellido_paterno',max_length=250)
    apellido_materno = models.CharField('apellido_materno',max_length=250)
    fecha_naciemento = models.DateField('fecha_naciemento', auto_now=False, auto_now_add=False,null=True)
    direccion = models.CharField('direccion',max_length=250,null=True)
    numero_celular = models.CharField('numero_celular',max_length=14)
    genero = models.CharField(max_length=1, choices=choices_genero, blank=True,null=True)
    roles_usuario= models.CharField(max_length=1,choices=choices_roles,default='U')
    codregistro = models.CharField(max_length=6, blank=True)
    usuario_pedido = models.ManyToManyField(pedido)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]
    objects = UserManager()
