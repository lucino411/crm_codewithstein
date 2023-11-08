from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    max_leads = models.IntegerField()
    max_clients = models.IntegerField()

    def __str__(self):
        return self.name


class Team(models.Model):
    plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
'''
Como el modelo Plan esta relacionado con Team, que ya existia en la base de datos, da un error al hacer la migracion porque no se puede agregar un valor vacio en Team, para esto agregamos un plan por el shell de Django asi:

(env) ➜  tealcrm git:(main) ✗ python manage.py makemigrations

It is impossible to add a non-nullable field 'plan' to team without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1
>>> from team.models import Plan
>>> plan = Plan.objects.create(name='Basic', price=10, max_leads=2, max_clients=2)
>>> exit()

Estamos creando un Plan llamado 'Basic' que cuesta 10 y tiene un maximo de leads de 2 y un maximo de clientes de 2
    
'''
    


    