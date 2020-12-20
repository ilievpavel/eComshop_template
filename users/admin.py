from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import UserProfile

UserModel = get_user_model()


class ProfileInlineAdmin(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInlineAdmin,
    )


admin.site.unregister(UserModel)
admin.site.register(UserModel, UserAdmin)
