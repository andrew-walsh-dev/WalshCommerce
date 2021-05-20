from django.shortcuts import render
from .models import Product

# Create your views here.
def store(req):
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }
    #pass in the products from database to be rendered
    return render(req, 'store/store.html', context)
    