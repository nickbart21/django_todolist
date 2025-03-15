from django.urls import path
from . import views

#from todolist.todolist.urls import urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete')
]