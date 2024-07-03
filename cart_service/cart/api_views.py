from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart
from .serializers import (CartItemSerializer, CartListSerializer,
                          CartCreateSerializer)
import requests


class CartListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer


class CartWithProducts(ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("Running CartWithProducts for User:", self.request.user)
        product_uri = "http://127.0.0.1:9090/api/product/list/"
        headers = {"Authorization": request.headers.get("Authorization")}
        response = requests.get(product_uri, headers=headers)
        if response.status_code != 200:
            return Response(
                {"error": "Failed to fetch products"},
                status=response.status_code,
            )
        products = response.json()
        cart_items = Cart.objects.filter(user=request.user)

        product_id_to_name = {item["id"]: item["name"] for item in products}
        for c_item in cart_items:
            c_item.product_name = product_id_to_name.get(c_item.product_id, "")

        return Response(CartItemSerializer(cart_items, many=True).data)


class CartCreateAPIView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
