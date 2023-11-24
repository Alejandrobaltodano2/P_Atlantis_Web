from django.shortcuts import render

# Create your views here.
from ..Chatbot.funciones import RespuestaChatBOt
#Vista Para crear al usuario

def Index(request):
    template_name = "inicio/index.html"
    return RespuestaChatBOt(request=request,templane_name=template_name)

    


