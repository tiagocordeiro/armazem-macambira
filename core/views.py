from django.shortcuts import render
from products.facade import get_all_categories


def index(request):
    categorias = get_all_categories()
    ctx = {'categorias': categorias, }
    return render(request, 'index.html', context=ctx)
