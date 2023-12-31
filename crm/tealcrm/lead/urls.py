from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.LeadListView.as_view(), name='list'),
    # path('', views.leads_list, name='list'),
    path('<int:pk>/', views.leads_detail, name = 'detail'),
    path('<int:pk>/delete/', views.leads_delete, name = 'delete'),
    path('<int:pk>/edit/', views.leads_edit, name = 'edit'),
    path('<int:pk>/convert/', views.convert_to_client, name ='convert'),
    path('add/', views.add_lead, name = 'add'),
]