from django.urls import path
from . import views

urlpatterns = [
    path('v1/meowjapan/<str:pk>/', views.LandingAPIDetail.as_view(), name='meowjapan-detail'),
    path('v1/meowjapan/', views.LandingAPI.as_view(), name='meowjapan-list'),
]
