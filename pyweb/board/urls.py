from django.contrib import admin
from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path("<int:question_id>", views.detail, name='detail')
]
