from django.urls import path, include

from product import views

urlpatterns = [
    path('big-categories/', views.BigCategoriesList.as_view()),
    path('categories/<slug:big_category_slug>/', views.CategoriesList.as_view()),
    path('latest-products/', views.LatestProductsList.as_view()),
    path('product/<slug:big_category_slug>/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view()),
    path('products/<slug:big_category_slug>/<slug:category_slug>/', views.CategoryProductsList.as_view()),
]