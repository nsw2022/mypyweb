from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from common.forms import UserForm


# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)  # 데이터가 입력된 폼
        if form.is_valid():
            form.save()  # 회원가입을 DB에 저장

            username = form.cleaned_data('username')
            password = form.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')  # index 페이지
    else:
        form = UserForm()  # 빈폼 생성
    context = {'form': form}
    return render(request, 'common/signup.html', context)
