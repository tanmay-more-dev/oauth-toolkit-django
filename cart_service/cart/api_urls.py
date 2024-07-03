from django.urls import path
from .api_views import (CartListAPIView, CartWithProducts,
                        CartCreateAPIView)


app_name = "cart"

urlpatterns = [
    path("list/", CartListAPIView.as_view(), name="list"),
    path("products/", CartWithProducts.as_view(), name="list_products"),
    path("products/create/", CartCreateAPIView.as_view(), name="add_products"),
]
