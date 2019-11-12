from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Item Admin Definition """

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
        "host",
    )

    list_filter = ("country", "city")

    search_fields = ("^city", "host__username")


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
