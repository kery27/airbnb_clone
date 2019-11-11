from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Item Admin Definition """

    pass


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
