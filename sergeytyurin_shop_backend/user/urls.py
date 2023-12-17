from django.urls import path, include

from user import views

urlpatterns = [
    path('user/get_user_id/<slug:token>/', views.UserIdDetail.as_view()),
    path('client/<slug:user_id>/info/', views.ClientInformationDetail.as_view()),
]