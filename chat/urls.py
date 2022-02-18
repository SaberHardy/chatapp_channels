from django.urls import path, re_path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:room_name>/', views.room, name='room'),
]
