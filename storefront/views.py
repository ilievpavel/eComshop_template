from django.shortcuts import render

from store.models import Product


def home_page(request):
    context = {
        'products': Product.objects.all(),
    }

    return render(request, 'index.html', context)
