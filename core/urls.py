from django.urls import path, include
from rh-desafio.core import view


app_name = 'core'

urlpatterns = [
   path('process-list-full/', views.ProcessList, name='process-list'),
   # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
   # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
   path('process-create/', views.ProcessCreate, name='create'),
   # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
   path('process-update/<id>', views.ProcessUpdate, name='process-update'),
   path('process-delete/<id>', views.ProcessDelete, name='process-delete'),


]