from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from XplrBg.accounts.forms import UserRegistrationForm, ProfileEditForm
from XplrBg.accounts.models import UserProfile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'is_staff',]
    list_filter = ()
    add_form = UserRegistrationForm
    readonly_fields = ('date_joined', 'last_login',)
    fieldsets = (
        (None, {"fields": ()}),
        ("Personal info", {"fields": ("email",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", 'is_staff'),
            },
        ),
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name",),
            },
        ),
    )


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('first_name',)
    list_display = ['first_name', 'last_name', 'lives_at', 'profile_image', 'user']
    add_form = ProfileEditForm
    list_filter = ('lives_at', )
    search_fields = ('first_name', 'last_name', 'user__email', 'lives_at', )
    sortable_by = ('id', 'first_name', 'last_name')