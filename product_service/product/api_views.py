from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get(self, request, *args, **kwargs):
        print("Running ProductListAPIView for User:", self.request.user)
        return super().get(request, *args, **kwargs)


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
