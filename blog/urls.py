from django.urls import path
from . import views


urlpatterns = [

    path('create/',views.create_view, name = 'create-path'),
     path('',views.list_view, name = 'home-path'),
     path('list/<int:post_pk>',views.detail_view, name = 'detail-path'),
     path('update/<int:post_pk>',views.update_view, name = 'update-path'),
     path('delete/<int:post_pk>',views.delete_view, name = 'delete-path'),

]

