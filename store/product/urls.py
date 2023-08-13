from django.urls import path
from .views import ProductList,ProductCategoryList,ProductDetail,ProductCategoryDetail,CategorySearchView

urlpatterns = [
    path('product-category/', ProductCategoryList.as_view(), name='product-category-list'),
    path('product-category/<int:pk>/', ProductCategoryDetail.as_view(), name='product-category-detail'),
    path('product-category/search/', CategorySearchView.as_view(), name='product-category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]