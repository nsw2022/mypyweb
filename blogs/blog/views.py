from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone


def index(request):
    # 최신글 3개 보여주기
    recent_post = Post.objects.order_by('-pub_date')[0:3]
    context = {'recent_post': recent_post}
    return render(request, 'blog/index.html', context)


# 포스트 목록
def post_list(request):
    post_list = Post.objects.order_by('-pub_date')

    # 검색처리
    kw = request.GET.get('kw', '')

    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |  # 제목으로 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw)  # 글쓴이

        ).distinct()

    # 페이지
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    page_obj = paginator.get_page(page)

    categories = Category.objects.all()
    context = {
        'post_list': page_obj,
        'categories': categories,
        'post_list2': len(post_list),
        'kw': kw
    }
    return render(request, 'blog/post_list.html', context)


# 포스트 상세 페이지
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()
    context = {'post': post, 'categories': categories}
    return render(request, 'blog/detail.html', context)

@login_required(login_url='common:login')
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)


# 카테고리 페이지
def category_page(request, slug):
    current_category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=current_category)  # 현재 카테고리의 포스트
    post_list = post_list.order_by('-pub_date')  # 날짜순 내림 차순
    post_list2 = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'current_category': current_category,
        'post_list': post_list,
        'categories': categories,
        'total_post': len(post_list),
        'post_list2': len(post_list2)

    }
    return render(request, 'blog/post_list.html', context)


# 포스트 삭제
@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:post_list')

# 댓글 생성
@login_required(login_url='common:login')
def comment_create(request, post_id):
    post = Post.objects.get(id=post_id) # 댓글을 쓰기 위한 포스트 한개를 가져옴
    if request.method=='POST':
        form = CommentForm(request.POST) # 입력된 댓글 가져옴
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author = request.user # 로그인한 글쓴이
            comment.pub_date = timezone.now() # 댓글 작성일과 시간
            comment.post = post
            form.save() # 실제저장
            return redirect('blog:detail', post_id=post_id)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment=Comment.objects.get(id=comment_id) # 아이디가 맞는 댓글하나 가져와서
    comment.delete() # 지움
    return redirect('blog:detail', post_id=comment.post_id)

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = Comment.objects.get(id=comment_id)  # 아이디가 맞는 댓글하나 가져와서
    if request.method == "POST":
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('blog:detail',post_id=comment.post_id)
    else:
        form = CommentForm(instance=comment)
    context = {'form':form,'comment':comment}
    return render(request, 'blog/comment_form.html', context)