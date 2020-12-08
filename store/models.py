from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, blank=False)


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(default=0.00)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='products', blank=False)

    manufacturers = Manufacturer.objects.all()

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
