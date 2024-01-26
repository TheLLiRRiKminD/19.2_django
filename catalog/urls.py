from django.urls import path
from .views import ProductListView, contacts, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
