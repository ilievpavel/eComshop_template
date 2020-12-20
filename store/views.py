from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from store.forms import CreateForm
from store.models import Product, Manufacturer


# Product views:
from users.decorators import user_required


@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'price', 'description', 'image', 'manufacturer']
    template_name = 'products/product_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductCreate, self).form_valid(form)


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_required(Product), name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products/product_update.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_required(Product), name='dispatch')
# @method_decorator(user_required(Product), name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('home')
    template_name = 'products/product_delete.html'


# Manufacturer views:
@method_decorator(login_required, name='dispatch')
class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'manufacturer_form.html'


class ManufacturerDelete(DeleteView):
    model = Manufacturer
    template_name = 'manufacturer_form.html'
    success_url = reverse_lazy('/')
