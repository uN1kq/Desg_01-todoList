from django.urls import path
from . import views

#routing the views through the URL 

urlpatterns = [
    path('',views.lists, name='lists'),
    path('updateList/<str:pk>/', views.updateList, name='updateList'),
    path('deleteItem/<str:pk>/', views.deleteItem, name='deleteItem'),
]

