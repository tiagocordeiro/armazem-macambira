from django.shortcuts import render
from products.facade import get_product, get_products_category


def product_list(request):
    return render(request, 'products/product_list.html')


def product_detail(request, slug):
    produto = get_product(slug)
    categoria = produto.category.slug
    ctx = {'produto': produto,
           'categoria': categoria}
    return render(request, 'products/product_detail.html', context=ctx)


def category_list(request, slug):
    produtos_categoria = get_products_category(slug)
    ctx = {'produtos_categoria': produtos_categoria, }
    return render(request, 'products/category_list.html', context=ctx)
