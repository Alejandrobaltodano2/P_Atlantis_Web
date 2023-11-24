from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.generic import (
    View,
    TemplateView,
    DeleteView
)
from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm
)
from .models import User
from .functions import code_generator
from django.shortcuts import render


class RegisterUserView(FormView):
    template_name = 'users/register_user.html'
    form_class = UserRegisterForm
    success_url='/'
    def form_valid(self, form) :
        #codigo
        codigo = code_generator()
        usuario = User.objects.create_user( 
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
            dni = form.cleaned_data['dni'],
            #nombre=form.cleaned_data['nombre'],
            #apellido_paterno=form.cleaned_data['apellido_paterno'],
            #apellido_materno=form.cleaned_data['apellido_materno'],
            numero_celular=form.cleaned_data['numero_celular'],     
            codregistro=codigo
        )
        asunto  = 'Confirmacion de Email'
        mensaje = 'Codigo de verificacion '+codigo 
        email_remitente = 'arturo948661842@gmail.com'
        send_mail(asunto,mensaje,email_remitente, [form.cleaned_data['email'],])
        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification',
                kwargs={'pk':usuario.pk}
            )
        )
    
class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index_app:inicio')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


#
class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )

class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('index_app:inicio')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        #
        User.objects.filter(
            pk=self.kwargs['pk']
        ).update(
            is_active=True
        )
        return super(CodeVerificationView, self).form_valid(form)
