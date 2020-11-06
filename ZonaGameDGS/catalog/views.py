from django.shortcuts import render
from .models import Juego, Genre
from django.views import generic
# Create your views here.
def index(request):
    num_Juego=Juego.objects.all().count()

    

    return render(
      request,
       'index.html',
       context={'num_Juego':num_Juego},
      )
class JuegoDetailView(generic.DetailView):
    model = Juego
	
	class CreateJuego(CreateView):
    model = contacto
    fields = 'all'
    initial = {'name', 'email', 'telefono', 'massage'}

class ContactoUpdate(UpdateView):
    model = contacto
    fields = {'name', 'email', 'telefono', 'massage'}

class ContactoDelete(DeleteView):
    model = contacto
    sucess_url = reverse_lazy('contactos')

class ContactoDetailView(generic.DetailView):
    model = contacto