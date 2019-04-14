from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from core.models import Active, TimeStampedModel


class Product(TimeStampedModel, Active):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug / URL",
                            help_text="Preenchido automaticamente, não editar.",
                            null=True,
                            blank=True, )
    description = models.TextField()
    image = models.ImageField(verbose_name="Imagem", upload_to='produtos/', null=True, blank=True, )
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, )

    class Meta:
        ordering = ('name',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(TimeStampedModel, Active):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug / URL",
                            help_text="Preenchido automaticamente, não editar.",
                            null=True,
                            blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(verbose_name="Imagem", upload_to='categoria-produtos/', null=True, blank=True, )

    class Meta:
        ordering = ('name',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def get_absolute_url(self):
        return reverse('category_list', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
