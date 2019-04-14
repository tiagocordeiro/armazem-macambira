from django.urls import path

from . import views

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produto/<slug>/', views.product_detail, name='product_detail'),
    path('categorias/', views.categories_list, name='categories_list'),
    path('<slug>/', views.category_list, name='category_list'),
]
