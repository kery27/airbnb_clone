from django.urls import path
from . import views

app_name = "rooms"
# 뷰의 룸 디테일 함수를 호출하게 될꺼야

# url dispatcher가 존재함 주소뒤에 변수를 오게 할수 있음

urlpatterns = [
    path("create/", views.CreateRoomView.as_view(), name="create"),
    path("<int:pk>/", views.RoomDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditRoomView.as_view(), name="edit"),
    # path("search/", views.search, name="search"),
    path("<int:pk>/photos/", views.RoomPhotosView.as_view(), name="photos"),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path("search/", views.SearchView.as_view(), name="search"),
    path("<int:pk>/photos/add", views.AddPhotoView.as_view(), name="add-photo"),
]
