from django.shortcuts import render, redirect
from api.models import Event
from api.forms import EventForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login ,logout# funcao que salva o usuario na sessao



from .serializers import EventSerializerModel

@login_required
def home(request):
	events = Event.objects.all()
	context = {
	'events':events,
	}
	return render(request, 'index.html',context)

@login_required
def addEvent(request):
	if(request.method == 'POST'):
		eventForm = EventForm(request.POST)
		if eventForm.is_valid():
			event = eventForm.save(commit = False)
			event.owner = request.user
			event.save()
			messages.success(request, 'Evento cadastrado com sucesso.')
			return HttpResponseRedirect(reverse('home'))
	context = {
	'formLocal':EventForm,
	}		
	return render(request, 'cadastrarLocal.html',context)

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')

def addUser(request):
    # Se dados forem passados via POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados 
            return HttpResponseRedirect("/login/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "addUser.html", {"form": form})
    
    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "addUser.html", {"form": UserCreationForm() })

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            #agora, basta logar o usuario e ser feliz.
            login(request, form.get_user())
            return HttpResponseRedirect("/index.html") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "login.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "login.html", {"form": AuthenticationForm()})


from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import Http404

class EventsRest(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def get(self, request):
		events = Event.objects.all()
		serializer = EventSerializerModel(events,many=True)
		print(serializer)
		return JsonResponse(serializer.data,safe=False)