from django.urls import path

from base import views

app_name = "base"

urlpatterns = [
    path("products/", views.list_products, name="list-products"),
    path("products/<str:pk>/", views.get_product, name="detail-product"),
]
