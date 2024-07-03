from django.urls import path
from .api_views import ProductListAPIView, ProductRetrieveAPIView


app_name = "product"

urlpatterns = [
    path("list/", ProductListAPIView.as_view(), name="list"),
    path("<int:pk>/detail", ProductRetrieveAPIView.as_view(), name="retrieve"),
]
