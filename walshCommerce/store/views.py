from django.shortcuts import render

# Create your views here.
def store(req):
    return render(req, 'store/store.html')