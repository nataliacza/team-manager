from django.urls import path
from register.views import HomeView, DogListView, TeamListView, EquipmentListView

app_name = "register"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    path("zespol/", TeamListView.as_view(), name="zespol"),
    path("psy/", DogListView.as_view(), name="psy"),
    path("sprzet/", EquipmentListView.as_view(), name="sprzet")
]
