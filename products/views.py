from django.shortcuts import render
from products.facade import get_product, get_products_category

from products.facade import get_all_categories


def product_list(request):
    return render(request, 'products/product_list.html')


def product_detail(request, slug):
    produto = get_product(slug)
    categorias = get_all_categories()
    categoria = produto.category.slug
    ctx = {'produto': produto,
           'categoria': categoria,
           'categorias': categorias}
    return render(request, 'products/product_detail.html', context=ctx)


def category_list(request, slug):
    produtos_categoria = get_products_category(slug)
    categorias = get_all_categories()
    categoria = slug
    ctx = {'produtos_categoria': produtos_categoria,
           'categorias': categorias,
           'categoria': categoria}
    return render(request, 'products/category_list.html', context=ctx)


def categories_list(request):
    categorias = get_all_categories()
    ctx = {'categorias': categorias, }
    return render(request, 'products/categories.html', context=ctx)
