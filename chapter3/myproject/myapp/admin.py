from django.contrib import admin

# Register your models here.
from .models import Book

# 사용자의 요구에 더 잘 맞도록 외관이나 동작을 사용자화해야 할 수도 있습니다.
# @admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author')
    # BookAdmin에서 status 필드에 대한 목록 필터를 추가할 수 있습니다.
    list_filter = ('status')

    # 선택된 도서를 게시된 것으로 표시하는 Book 모델에 작업을 추가할 수 있습니다.
    actions = ('mark_as_published')

    def mark_as_published(self, request, queryset):
        queryset.update(status='p')

    mark_as_published.short_description = "선택된 도서를 게시된 것으로 표시"

    




admin.site.register(Book)