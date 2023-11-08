from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import AddLeadForm
from .models import Lead

from client.models import Client
from team.models import Team



class LeadListView(ListView):
    model = Lead
    
    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        queryset = queryset.filter(created_by=self.request.user, converted_to_client=False)

        return queryset   



# @login_required
# def leads_list(request):
#     leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)

#     return render(request, 'lead/leads_list.html', {'leads': leads})


@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    # lead = Lead.objects.filter(created_by=request.user).get(pk=pk) # de esta forma solo el usuario que creo el lead puede modificarla
    lead = Lead.objects.get(pk=pk)

    return render(request, 'lead/leads_detail.html', {'lead': lead})


@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, "Lead deleated")

    return redirect('leads:list')


@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            lead.save()

            messages.success(request, "Lead was edited")

            return redirect('leads:list')
    else:
        form = AddLeadForm(instance=lead)

    return render(request, 'lead/leads_edit.html', {'form': form})


@login_required
def add_lead(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = team
            lead.save()

            messages.success(request, "Lead was created")

            return redirect('leads:list')
    else:
        form = AddLeadForm()

    return render(request, 'lead/add_lead.html', {'form': form, 'team': team})

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]
    
    Client.objects.create(
        name=lead.name, 
        email=lead.email, 
        description=lead.description,
        created_by=request.user,
        team = team,
    )

    lead.converted_to_client = True
    lead.save()

    messages.success(request, "The lead was converted to Client successfully")

    return redirect('leads:list')



'''
La línea lead = form.save(commit=False) se utiliza para crear una instancia del modelo antes de guardarla en la base de datos. Al llamar a form.save(commit=False), se crea un objeto que aún no se ha guardado en la base de datos, lo que te permite realizar modificaciones adicionales en el objeto antes de guardar los cambios.

En este código específico, se está asignando el campo created_by del modelo Lead al usuario que ha enviado el formulario, utilizando request.user. Después de realizar esta modificación en el objeto lead, se guarda en la base de datos utilizando lead.save()

Esta técnica es útil cuando necesitas realizar modificaciones o cálculos adicionales en el objeto antes de guardarlo en la base de datos. Al utilizar commit=False, puedes controlar la lógica relacionada con el modelo y personalizar cualquier campo adicional antes de persistir los datos.
'''
