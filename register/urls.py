from django.urls import path
from register.views import (HomeView, TeamListView, DogListView, FleetListView, EquipmentListView,
                            MemberCreateView, DogCreateView)

app_name = "register"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    path("zespol/", TeamListView.as_view(), name="zespol"),
    path("psy/", DogListView.as_view(), name="psy"),
    path("psy/dodaj-psa/", DogCreateView.as_view(), name="dodaj-psa"),
    path("flota/", FleetListView.as_view(), name="flota"),
    path("sprzet/", EquipmentListView.as_view(), name="sprzet"),
    path("zespol/dodaj-czlonka/", MemberCreateView.as_view(), name="dodaj-czlonka"),
]
