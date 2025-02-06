from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "role")
    search_fields = ("user_name",)
    list_filter = ("role",)
