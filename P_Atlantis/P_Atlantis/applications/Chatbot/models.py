from django.db import models
from django.conf import settings

class PreguntaChat(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pregunta = models.CharField('pregunta_al_bot', max_length=1500)
# Create your models here.

class RespuestasGenericas(models.Model):
    respuesta = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="imagenes",blank=True)
    musica = models.FileField(upload_to="mp3",max_length=250,blank=True)
class RespuestaChatBot(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    pregunta = models.ForeignKey(PreguntaChat, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(RespuestasGenericas,on_delete=models.CASCADE,null=True)

