from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "article", "created_at")  # ✅ Заменили "user" на "author"
    search_fields = ("author__user_name", "article__title")
    list_filter = ("created_at",)