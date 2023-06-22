from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()              # 내용
    pub_date = models.DateTimeField()         # 발행일
    # blank 는 입력 폼이 비어도 됨
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True, blank=True) # null 허용 파일을 첨부하지 않을수 있음

    # 이걸안하면 관리자 페이지에서 잘안나옴
    def __str__(self):
        return self.title
