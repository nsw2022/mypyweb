from django.contrib import admin

from blog.models import Post, Category

# Register your models here.
admin.site.register(Post)


# 카테고리 등록
class CategoryAdmin(admin.ModelAdmin):
    # slug와 name이 동시에 입력
    prepopulated_fields = {'slug': ('name',)} # name 은 튜플


admin.site.register(Category, CategoryAdmin)
