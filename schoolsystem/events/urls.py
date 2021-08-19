from django.urls import path
from . import views


urlpatterns=[

    path('register_event/',views.register_event,name='event'),
    path('event_list/',views.event_list,name='event_list'),
]
