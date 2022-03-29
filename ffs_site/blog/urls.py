from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/timeline/', views.timeline_view, name='timeline'),
    path('add-someone/', views.add_view, name='add_content'),
]