from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_user_family_name', 'display_user_surname', 'block', 'role', ]


admin.site.register(UserProfile, UserProfileAdmin)
