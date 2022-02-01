from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from solisite import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('solisite/', include('solisite.urls')),
]  
