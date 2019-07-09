from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

# 1차 url과 2차 url이 '' 때문에 서버에 접속 하면 바로 views.post_list가 실행
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]