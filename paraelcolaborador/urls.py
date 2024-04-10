from django.urls import path, include
from . import views


urlpatterns = [
  
    
    path('', views.paraelcolaborador, name="paraelcolaborador"),
    path('accounts/',include('django.contrib.auth.urls')),

    
]
