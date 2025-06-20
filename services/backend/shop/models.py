from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return sum(self.products.price)

    def get_qr_code(self):
        return self.customer_name

    def __str__(self):
        return f"Order from {self.customer_name}, {self.created}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.price} Kč ({self.count} pcs)"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    @property
    def price(self):
        return self.product.price * self.count

    def __str__(self):
        return f"{self.product.name}, {self.count} pcs, each for {self.product.price} Kč"