from django.urls import path, include

from order import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]