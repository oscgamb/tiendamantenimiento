from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.

@login_required
def paraelcolaborador(request):
    return render(request, 'paraelcolaborador/paraelcolaborador.html')

