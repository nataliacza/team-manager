from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from register.views import Error404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("error-404/", Error404.as_view(), name="error-404"),
    path("", include("register.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
