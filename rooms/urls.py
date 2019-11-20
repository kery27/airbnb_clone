from django.urls import path
from . import views

app_name = "rooms"
# 뷰의 룸 디테일 함수를 호출하게 될꺼야

# url dispatcher가 존재함 주소뒤에 변수를 오게 할수 있음

urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    # path("search/", views.search, name="search"),
    path("search/", views.SearchView.as_view(), name="search"),
]
