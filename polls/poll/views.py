from django.http import HttpResponse
from django.shortcuts import render

from poll.models import Question


def index(request):
    return render(request,'poll/index.html')

def poll_list(request):
    # 전체 데이터
    question_list = Question.objects.all()

    return render(request, 'poll/poll_list.html', {'question_list': question_list})
    # return HttpResponse("<h1>Hello Django~</h1>")


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question': question})


def test(request):
    cart = "콩나물"  # 모델(데이터) - 딕셔너리 형태로 보냄
    cartlist = ["계란", "콩나물", "생수", "커피"]
    context = {'cart': cart, 'cartlist': cartlist}
    return render(request, 'poll/test.html', context)


def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        try:
            choice_id = request.POST['choice']  # 선택된 항목 id
            sel_choice = question.choice_set.get(id=choice_id)  # id로 항목을 찾아서

        except: # 에러가 난 경우
            error = "선택을 하지 않았습니다."
            return render(request, 'poll/detail.html',
                          {
                              'question': question,
                              'error': error
                          })

        else:
            sel_choice.votes += 1  # 디폴트가 0 이므로
            sel_choice.save()  # 바뀐거 저장
    else:
        return render(request, 'polls/detail.html', id=question_id)  # 경로 유지

    return render(request, 'poll/result.html', {'question': question})
