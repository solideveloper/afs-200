
from django.urls import path
from . import views

app_name='events'
urlpatterns = [
    path('', views.events, name = "events"),
    path('<int:year>/<str:month>', views.events, name = "events"),
    path('events', views.all_events, name="list-events"),
]