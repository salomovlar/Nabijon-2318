from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('katalog/', views.katalog, name='katalog'),
    path('buyurtma/', views.buyurtma, name='buyurtma'),
    path('biz-haqimizda/', views.biz_haqimizda, name='biz_haqimizda'),
    path('api/books/', views.api_books, name='api_books'),
]
