from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)
    shop_id = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-id',)
