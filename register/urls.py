from django.urls import path
from register.views import HomeView

app_name = "register"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
]
