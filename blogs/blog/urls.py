from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'), # 메인 화면
    path('detail/<int:post_id>/', views.detail, name='detail'), # 포스트 상세보기
    path('post/create/', views.post_create, name='post_create'), # 포스트 생성
    path('category/<str:slug>/', views.category_page, name='category_page'), # 카테고리
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'), # 포스트 삭제

    path('comment/create/<int:post_id>', views.comment_create, name='comment_create'), # 댓글 생성
    path('comment/delete/<int:comment_id>', views.comment_delete, name='comment_delete'), # 댓글 삭제
    path('comment/modify/<int:comment_id>', views.comment_modify, name='comment_modify') # 댓글 삭제
]