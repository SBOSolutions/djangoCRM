from django.urls import path
from leads.views import lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path('', lead_list, name = 'lead-list'),
    path('create/', lead_create, name = 'lead-create'),
    path('<int:pk>/update/', lead_update, name = 'lead-update'),
    path('<int:pk>/delete/', lead_delete, name = 'lead-delete'),
    path('<int:pk>', lead_detail, name = 'lead-detail')
]