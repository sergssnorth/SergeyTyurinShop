from django.urls import path, include

from product import views

urlpatterns = [
    path('user/get_user_id/<slug:token>/', views.UserIdDetail.as_view()),
    path('client/<slug:user_id>/info/', views.ClientInformationDetail.as_view()),
    path('latest-products/', views.LatestProductsList.as_view()),
    path('product/<slug:big_category_slug>/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view()),
    path('products/<slug:big_category_slug>/<slug:category_slug>/', views.CategoryProductsList.as_view()),
    path('categories/<slug:big_category_slug>/', views.CategoriesList.as_view()),
]