from django.http import HttpResponse
from django.shortcuts import render

#from ShopApp.forms import FormCreateProduct, FormRawCreateProduct
#from ItemsApp.models import ModelProduct

# Create your views here.
# Use views here to handle request logic.

def viewTest(request, *args, **kwargs):
    currentUser = str(request.user)
    s1 = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    printThis = currentUser  + " || Authenticated: " + s1 + " || Args: " + s2 + " || Keyword Args: " + s3
    context = {
        "dingus": printThis
    }

    #return HttpResponse("<h1>Sample txt. Current user is: %s </h1>" % printThis)
    return render(request, "test.html", context)

def viewHome(request, *args, **kwargs):
    currentUser = str(request.user)
    s1 = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    printThis = currentUser  + " || Authenticated: " + s1 + " || Args: " + s2 + " || Keyword Args: " + s3
    context = {
        "dingus": printThis
    }
    return render(request, "home.html", context)

def viewCart(request, *args, **kwargs):
    currentUser = str(request.user)
    s1 = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    printThis = currentUser  + " || Authenticated: " + s1 + " || Args: " + s2 + " || Keyword Args: " + s3
    context = {           
        "dingus": printThis,
        "Greeting": ("Hello ", currentUser,"."),                                 
        "Example1": "This is the cart page.",
        "ExampleList1": [4, "long list", "of items"]
    }
    return render(request, "cart.html", context)