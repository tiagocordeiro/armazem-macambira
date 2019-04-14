from django.urls import path

from . import views

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produto/<slug>/', views.product_detail, name='product_detail'),
    path('<slug>/', views.category_list, name='category_list'),
]
