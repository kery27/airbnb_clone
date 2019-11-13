from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Item Admin Definition """

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

    search_fields = ("^city", "host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    # 셀프는 룸 옵젝트고 , obj는 현재줄을 말한다 currunt row
    def count_amenities(self, obj):
        return obj.amenities.all()

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

    pass
