from django.urls import path, include
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
  
    path('', views.home, name="Home"),
    path('accounts/',include('django.contrib.auth.urls')),
    

    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)