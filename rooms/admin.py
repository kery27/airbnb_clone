from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.

# 룸 어드민 안에서 포토 어드민을 관리 하는 기능의 시작
class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Item Admin Definition """

    # 룸 어드민안에서 포토를 관리하는 기능을 추가
    inlines = (PhotoInline,)

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "address")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guest", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "city",
        "country",
    )
    # 너무 많은 유저가 생기면 유저를 검색하는 창을 하나 띄워준다.
    raw_id_fields = ("host",)

    search_fields = ("^city", "host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    # 어드민에서의 저장시 이벤트를 다시씀
    # 리퀘스트를 가지고와서 어떤 유저가 저장을 하려고 하는지 확인 할 수도 있고
    # 어드민이 변경될경우에 메일로 보내서 추적할 수도 있다
    def save_model(self, request, obj, form, change):
        # print(obj, change, form)
        super().save_model(request, obj, form, change)

    # 셀프는 룸 옵젝트고 , obj는 현재줄을 말한다 currunt row
    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "hello kitty!"


# 룸타입을 어드민에 추가 해주는 작업..
@admin.register(
    models.RoomType, models.Amenity, models.HouseRule, models.Facility,
)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width ="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
