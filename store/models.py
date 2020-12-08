from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='products', blank=False)

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
