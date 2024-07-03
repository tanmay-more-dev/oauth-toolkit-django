from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    product_id = models.IntegerField()
    qty = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "".join([str(self.product_id), " - ", str(self.qty)])

    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ("-id",)
