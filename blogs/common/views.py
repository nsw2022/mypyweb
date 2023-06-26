from django.shortcuts import render, redirect

from .forms import UserForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST) # 폼에 입력된 데이터를 넘겨받음
        if form.is_valid(): # 유효성에 통과되면
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)

# 카테고리 페이지 처리 메서드