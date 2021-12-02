from django.urls import path
from register.views import HomeView

app_name = "register"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
]
