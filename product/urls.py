from django.urls import path
from product.views import ProductCreateView, ProductListView, ProductUpdateView

app_name = 'product'

urlpatterns = [
    path('p/create', ProductCreateView.as_view(), name='test'),
    path('p/list', ProductListView.as_view(), name='list'),
    path('p/update/<int:pk>', ProductUpdateView.as_view(), name='list'),
]