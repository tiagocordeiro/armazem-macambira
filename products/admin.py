from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
