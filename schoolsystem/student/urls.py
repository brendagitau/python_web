from django.urls import path
from .views import register_student
from .views import student_list
from .views import index
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    path('index/',index,name='index'),
    path('register/',register_student,name='register_student'),
    path('student_list/',student_list,name='student_list'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

