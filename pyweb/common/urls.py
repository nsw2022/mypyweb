from django.contrib.auth import views as auth_views
from django.urls import path
from common import views
app_name = 'common'

urlpatterns = [
    # 클래스형 LoginView를 사용
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #g 함수형 view사용
    path('signup/', views.signup, name='signup')
]
