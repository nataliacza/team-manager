from django.urls import path
from register.views import (HomeView,
                            TeamListView, DogListView, FleetListView, EquipmentListView,
                            MemberCreateView, DogCreateView, FleetCreateView,
                            MemberDetailView)

app_name = "register"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    path("zespol/", TeamListView.as_view(), name="zespol"),
    path("zespol/dodaj-czlonka/", MemberCreateView.as_view(), name="dodaj-czlonka"),
    path("zespol/<slug:slug>/", MemberDetailView.as_view(), name="szczegoly-czlonka"),
    path("psy/", DogListView.as_view(), name="psy"),
    path("psy/dodaj-psa/", DogCreateView.as_view(), name="dodaj-psa"),
    path("flota/", FleetListView.as_view(), name="flota"),
    path("flota/dodaj-pojazd/", FleetCreateView.as_view(), name="dodaj-pojazd"),
    path("sprzet/", EquipmentListView.as_view(), name="sprzet"),
]
