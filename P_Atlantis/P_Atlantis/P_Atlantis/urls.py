from django.contrib import admin
from django.urls import path,re_path, include
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("",include('applications.Users.urls')),
    #re_path("",include('applications.Platos.urls')),
    re_path("",include('applications.Inicio.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
