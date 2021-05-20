from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category

# Create your views here.
def store(req, category_slug=None):
    categories = None
    products = None

    #allow products to be filtered and shown by category
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }
    #pass in the products from database to be rendered
    return render(req, 'store/store.html', context)
    