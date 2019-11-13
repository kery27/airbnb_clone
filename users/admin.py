from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Register your models here.

# 어드민 패널에 이걸 추가해보고 싶다
# 어드민.모델어드민을 상속해서 리스트디스플레이 리스트 필터를 변형시켜서 사용해봈다.
###@admin.register(models.User)
###class CustomUserAdmin(admin.ModelAdmin):
###    """Custom User Admin"""
### admin.site.register(models.user, CustomUserAdmin) #위 어드민 레지스터의 기능과 같음
###    list_display = ("username", "gender", "language", "currency", "superhost")
###    list_filter = ("language", "superhost")
###


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Garcia info",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    # 상속받은 클래스에 기본적으로 적용된 리스트 필터에 추가된 슈퍼호스트 필터
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
