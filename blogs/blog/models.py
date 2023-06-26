from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)# unique->겹치면안됨
    # url 주소 - 문자, allow_unicode=True 한글 허용
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    # 카테고리 Url
    def get_absoulte_url(self):
        # return f'/blog/category/{self.slug}'
        return reverse('blog:category_page', args=[self.slug])

    # 관리자 페이지에서 적용
    class Meta:
        ordering = ['name'] # 이름순 정렬
        verbose_name = 'category'
        verbose_name_plural = 'categories'

# 포스트 모델
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()              # 내용
    pub_date = models.DateTimeField()         # 발행일
    # blank 는 입력 폼이 비어도 됨
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True, blank=True) # null 허용 파일을 첨부하지 않을수 있음
    # on_delete=models.SET_NULL -> 카테고리가(부모테이블의 요소가) 삭제될때 포스트는(자식요소는) 같이 삭제 되지 않는다
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    # 이걸안하면 관리자 페이지에서 잘안나옴
    def __str__(self):
        return self.title
