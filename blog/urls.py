from django.urls import path
from . import views


urlpatterns = [

    path('create/',views.create_view, name = 'create-path'),
     path('',views.list_view, name = 'home-path'),

]

