from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import(ListView,DeleteView,UpdateView)
from django.views.generic.edit import (FormView)
from ..Users.mixins import AdministradorPermisionMixin,UsuarioPermisionMixin
from django.views.generic import (
    View,
    TemplateView
    
)
from ..Chatbot.funciones import RespuestaChatBOt

class CreatePlatosView(AdministradorPermisionMixin,FormView):
    pass



def ejemplo(request):
    template_name = "platos/ejemplo.html"
    return RespuestaChatBOt(request=request,templane_name=template_name)