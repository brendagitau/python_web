from django.urls import path
from .views import course_form
from .views import course_list
urlpatterns=[
    path('course_form/',course_form,name='course_form'),
      path('course_list/',course_list,name='course_list'),
    ]