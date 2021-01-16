from django.urls import path
from leads.views import lead_list

app_name = "leads"

urlpatterns = [
    path('', lead_list)
]