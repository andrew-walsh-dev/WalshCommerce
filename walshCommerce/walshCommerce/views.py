from django.shortcuts import render
from store.models import Product

def homepage(req):
    #grab all products, then filter out non-availables
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    #pass in the list of products to render
    return render(req, 'index.html', context)
