from leads.views import landing
from django.contrib import admin
from django.urls import path, include
from leads.views import landing


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing-page"),
    path('leads/', include('leads.url', namespace="leads"))
]
