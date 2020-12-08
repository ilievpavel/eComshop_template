from django.contrib import admin

from store.models import Product, Manufacturer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_filter = ('title', 'price')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
