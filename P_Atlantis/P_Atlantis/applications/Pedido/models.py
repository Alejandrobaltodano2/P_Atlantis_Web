from django.db import models
from django.conf import settings

from ..Platos.models import Platos
# Create your models here.
class pedido_plato(models.Model):
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class pedido(models.Model):
    fecha_creacion = models.DateTimeField('fecha_creacion')
    plato_pedido = models.ForeignKey(pedido_plato, on_delete=models.CASCADE)
    pedido_usuario = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    precio_total = models.FloatField('precio_total',default=0)
    pedido_cancelado = models.BooleanField(default=False,null=True)
    metodo_pago = models.ImageField(upload_to='pedido',null=True)
    