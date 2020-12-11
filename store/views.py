from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from store.models import Product, Manufacturer


# Product views:

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-info')
    template_name = 'product_form.html'


# Manufacturer views:

class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = '__all__'
    template_name = 'manufacturer_form.html'


class ManufacturerDelete(DeleteView):
    model = Manufacturer
    template_name = 'manufacturer_form.html'
    success_url = reverse_lazy('/')
