from django.http import HttpResponse
from django.shortcuts import render

from .models import ModelProduct

# Create your views here.

def viewProductInfo(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3

    objRetrieved = ModelProduct.objects.get(name="the first") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

    context = {
        "dingus": userAndArgsInfo,
        "keyObj": objRetrieved,


        # "productName": objRetrieved.name,
        # "productImage": objRetrieved.image,
        # "productDescription": objRetrieved.description,
        # "productCategory": objRetrieved.category,
        # "productReleaseDate": objRetrieved.releaseDate,
        # "productCurrentStock": objRetrieved.currentStock,
        # "productManufacturer": objRetrieved.manufacturer,
        # "productPrice": objRetrieved.price,
    }

    return render(request, "ItemsApp/productInfo.html", context)

    