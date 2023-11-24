from django.shortcuts import render
from django.utils import timezone

from .models import PreguntaChat,RespuestaChatBot,RespuestasGenericas
from .funccionalidadBot import Chatbot
from ..Platos.models import Platos
from ..Pedido.models import pedido,pedido_plato

        
def Respuesta(pregunta:str):
    respuestas = RespuestasGenericas.objects.all()
    c=Chatbot(respuestas)
    i = int(c.Responder(pregunta))
    if i !=-1:
        return respuestas[i]
    return -1



def ProcesarPreguntaYrespuesta(request_pregunta,user):
    pregunta = PreguntaChat(usuario = user ,pregunta=request_pregunta)
    pregunta.save()
    pregunta_usuario = PreguntaChat.objects.filter(usuario = user,pregunta=request_pregunta)
    res = Respuesta(request_pregunta)
    if res !=-1:
        rp = RespuestaChatBot(usuario = user,pregunta =pregunta_usuario[0],respuesta=res)
        rp.save()
    else:
        rp = RespuestaChatBot(usuario = user,pregunta =pregunta_usuario[0],respuesta=None)
        rp.save()
def Procesar_Chat(request):
    def Clave_valor(texto:list):
        diccionario ={'ID':None,'cantidad':None,'LLevar':None,'delivery':None}

        for e in texto.strip().split(','):
            e = e.split(':')
            diccionario[e[0]]=e[1]
        return diccionario        

    elementos = request.strip().split(';')
    elementos_pedido = []
    elementos =elementos[1:]

    for e in elementos:
        if(len(e.split(','))==2):
            diccionario = Clave_valor(e)
            elementos_pedido.append(diccionario)
    return elementos_pedido

def RespuestaChatBOt(request ,templane_name):
    mensaje = request.POST.get('chat-input', '')
   
    context={}
    if len(mensaje) !=0:
        try:
            user =  request.user
            contexto = Procesar_Chat(mensaje)
            print(contexto)
            if contexto != []:
                precio_total =0
                for e in contexto:
                    #if e['cantidad'] >0 and type(e['cantidad']) ==int :
                    
                    platos = Platos.objects.filter(pk=e['ID'])
                    pedidoPlato = pedido_plato()
                    pedidoPlato.plato = platos[0]
                    pedidoPlato.cantidad = e['cantidad']
                    pedidoPlato.save()
                    precio = float(e['cantidad'])*platos[0].precio
                    pedidoUser = pedido()
                    pedidoUser.fecha_creacion = timezone.now()
                    pedidoUser.plato_pedido=pedidoPlato
                    pedidoUser.pedido_usuario=user
                    pedidoUser.precio_total = pedidoUser.precio_total +precio
                    precio_total = pedidoUser.precio_total
                    pedidoUser.save()
                messageUser = '''
                                Su pedido ha sido creado satisfactoriamente,
                                Su precio total es {},  esto no incluye el delivery y los tapers, se le llegara un mensaje a su whatssap o correo sobre el total y la coordinacion de su pedido gracias 
                                '''.format(precio_total)

                #context = {'pregunta_respuesta': union}
                context={'pregunta':mensaje,'respuesta':messageUser}
        
            else:   
                if(mensaje=='borra'):
                    PreguntaChat.objects.filter(usuario=user).all().delete()
                    context = {'user_pregunta': ''}
                
                if ("pedido" in mensaje):
                    user =  request.user
                    pedidos = pedido.objects.filter(pedido_usuario=user)
                    union = zip(mensaje,pedidos)
                    context = {'Ver_pedidos': union}

                else:
                    
                    ProcesarPreguntaYrespuesta(user=user,request_pregunta=mensaje)
                    pregunta = PreguntaChat.objects.filter(usuario=user)
                    respuesta1 = RespuestaChatBot.objects.filter(usuario = user)
                    union = zip(pregunta,respuesta1)
                    context = {'pregunta_respuesta': union}
        except:
            pass
            
    else:
        user =  request.user
        try:

            pregunta = PreguntaChat.objects.filter(usuario=user)
            respuesta1 = RespuestaChatBot.objects.filter(usuario = user)
            union = zip(pregunta,respuesta1)
            context = {'pregunta_respuesta': union}
        except:
            pass
    return render(request, templane_name, context)