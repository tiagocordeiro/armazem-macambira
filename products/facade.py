from .models import Product, Category


def get_all_products():
    """
    Search all products on database
    :return: tuple of Products
    """
    return tuple(Product.objects.all())


def get_product(slug):
    return Product.objects.get(slug=slug)


def get_all_categories(active=True):
    """
    Search all categories on database
    :return: tuple of Categories
    """
    if active is False:
        return tuple(Category.objects.all())
    return tuple(Category.objects.all().filter(active__exact=True))


def get_products_category(slug):
    return tuple(Product.objects.all().filter(category__slug__exact=slug))
