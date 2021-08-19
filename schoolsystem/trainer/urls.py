from django.urls import path
from .views import register_trainer, trainer_list
appname="trainer"

urlpatterns=[
    path('register_trainer/',register_trainer,name='register_trainer'),
    path('trainer_list/',trainer_list,name='trainer_list'),
    
]