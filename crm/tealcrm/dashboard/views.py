from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from client.models import Client
from team.models import Team
'''
La anotación @login_required en Django es un decorador que se utiliza en las vistas para restringir el acceso a usuarios no autenticados. Si un usuario no está autenticado e intenta acceder a una vista decorada con @login_required, Django redirigirá al usuario a la página de inicio de sesión. Esto garantiza que las vistas solo sean accesibles para usuarios autenticados.
'''


@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)[0]

    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]
    return render(request, 'dashboard/dashboard.html', {'leads': leads, 'clients' : clients})
