from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('read/', views.read_products),
    path('update/<int:product_id>/', views.update_product),
    path('delete/<int:product_id>/', views.delete_product),
]
