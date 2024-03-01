from django.urls import path

from jihanki import views

urlpatterns = [
  path("", views.product_list, name="product_list"),
  path("buy/<int:pk>/", views.buy_product, name="buy_product")
]
