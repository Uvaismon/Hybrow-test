from django.urls import path
from .views import (ProductPage, NewProduct, EditProduct, DeleteProduct,
                    LocationPage, NewLocation, EditLocation, DeleteLocation,
                    MovementPage, NewMovement, EditMovement, DeleteMovement,
                    Summary, Home)

urlpatterns = [
    path('products', ProductPage.as_view(), name='products'),
    path('new-product', NewProduct.as_view(), name='new_product'),
    path('edit-product/<pk>', EditProduct.as_view(), name='edit_product'),
    path('delete-product/<pk>', DeleteProduct.as_view(), name='delete_product'),

    path('locations', LocationPage.as_view(), name='locations'),
    path('new-location', NewLocation.as_view(), name='new_location'),
    path('edit-location/<pk>', EditLocation.as_view(), name='edit_location'),
    path('delete-location/<pk>', DeleteLocation.as_view(), name='delete_location'),

    path('movements', MovementPage.as_view(), name='movements'),
    path('new-movement', NewMovement.as_view(), name='new_movement'),
    path('edit-movement/<pk>', EditMovement.as_view(), name='edit_movement'),
    path('delete-movement/<pk>', DeleteMovement.as_view(), name='delete_movement'),

    path('summary', Summary.as_view(), name='summary'),
    path('', Home.as_view(), name='home'),
]
