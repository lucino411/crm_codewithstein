from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Userprofile
from team.models import Team

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            team = Team.objects.create(name='The team name', created_by=request.user)
            team.members.add(request.user)
            team.save()
            
            Userprofile.objects.create(user=user)

            return redirect('/log-in/')
    else:
        form = UserCreationForm()   

    return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]
    return render(request, 'userprofile/myaccount.html' ,{'team': team})


'''
En tu vista signup, estás procesando una solicitud POST y creando un nuevo usuario en tu base de datos.

Si el método de solicitud no es POST, el código en el else se ejecutará. form = UserCreationForm() crea una instancia del formulario UserCreationForm vacío para enviar al template. Esto permitirá que el template muestre un formulario en blanco para que el usuario complete sus datos y se registre.

Si el método de solicitud es POST, el formulario se valida y se crea un nuevo usuario en la base de datos. Si el método de solicitud no es POST, se muestra un formulario vacío para que el usuario complete sus datos.

El comando render renderiza un template con los datos proporcionados. En este caso, render toma tres argumentos:

request: el objeto de solicitud HTTP.
'userprofile/signup.html': la ruta al template que se renderizará.
{'form': form}: un diccionario que contiene el formulario que se mostrará en el template. En este caso, 'form' es el nombre de la variable que se utilizará en el template y form es el formulario que se pasará al template.

form es un objeto que representa el formulario y se pasará al template. Si el método es POST, se llenará con los datos del formulario enviado por el usuario. Si el método no es POST, estará vacío y listo para que el usuario complete el formulario.

'''
