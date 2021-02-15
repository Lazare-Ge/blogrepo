from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
