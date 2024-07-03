from rest_framework.serializers import (ModelSerializer, CharField,
                                        ValidationError, IntegerField)
from .models import Cart
import requests


class CartListSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(ModelSerializer):
    product_name = CharField()

    class Meta:
        model = Cart
        exclude = ('user',)


class CartCreateSerializer(CartListSerializer):
    user = IntegerField(write_only=True, required=False)

    def validate(self, attrs):
        product_id = attrs['product_id']
        uri = f'http://127.0.0.1:9090/api/product/{product_id}/detail'
        headers = {"Authorization":
                   self.context['request'].headers.get("Authorization")}
        response = requests.get(uri, headers=headers)
        if response.status_code != 200:
            raise ValidationError(
                {"error": "Unable to proceed. Check product Id."})
        attrs['user'] = self.context['request'].user
        return super().validate(attrs)
