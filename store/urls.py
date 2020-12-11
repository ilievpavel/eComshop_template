from django.urls import path

from store.views import ProductCreate, ProductUpdate, ProductDelete, ManufacturerCreate, ManufacturerDelete

urlpatterns = [
    path('product/add/', ProductCreate.as_view(), name='product-add'),
    path('product/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product-delete'),
    path('manufacturer/add/', ManufacturerCreate.as_view(), name='manufacturer-add'),
    path('manufacturer/<int:pk>/delete/', ManufacturerDelete.as_view(), name='manufacturer-delete'),
]
