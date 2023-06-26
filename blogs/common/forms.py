from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Mata:  # 정보라는 뜻
        model = User
        fields = ('username', 'email')  # 튜플 구조 (수정 금지)
        labels = {
            'title': '제목',
            'content': '내용',
            'photo': '사진'
        }
