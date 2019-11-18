from django.urls import path
from rooms import views as rooms_views

app_name = "core"

urlpatterns = [path("", rooms_views.HomeView.as_view(), name="home")]
