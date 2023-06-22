from django.contrib import admin
from django.urls import path
from board import views



app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),                  # 질문 등록

    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),      # 답변 등록
    path('answer/delete/<int:answer_id>/',views.answer_delete, name = 'answer_delete'),     # 답변 삭제


    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'), # 질문 삭제
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),  # 질문 수정

]
