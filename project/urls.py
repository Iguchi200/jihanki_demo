from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path("admin/", admin.site.urls),
  path("jihanki/", include("jihanki.urls"), name="product_list"),
]
