from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add-someone/', views.add_view, name='add_content'),
    path('add-form/', views.add_form_view, name='add_form'),
]