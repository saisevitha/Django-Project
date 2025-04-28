from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('myapi/create/', ProductCreateView.as_view(), name='create_product'),
    path('myapi/read/', ProductListView.as_view(), name='read_products'),
    path('myapi/update/<int:product_id>/', ProductUpdateView.as_view(), name='update_product'),
    path('myapi/delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete_product'),
]
