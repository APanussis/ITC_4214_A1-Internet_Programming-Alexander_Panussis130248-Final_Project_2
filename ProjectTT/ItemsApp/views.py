from django.http import HttpResponse
from django.shortcuts import render

from .forms import FormProductCreate
from .models import ModelProduct


# Create your views here.

def viewProductCreate(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    formRetrieved = FormProductCreate(request.POST or None)
    if formRetrieved.is_valid():
        formRetrieved.save()

    context = {
        "dingus": userAndArgsInfo,
        "keyForm": formRetrieved,
    }

    return render(request, "ItemsApp/productCreate.html", context)

def viewProductInfo(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    objRetrieved = ModelProduct.objects.get(name="5th test with no image") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

    context = {
        "dingus": userAndArgsInfo,
        "keyObj": objRetrieved,
    }

    return render(request, "ItemsApp/productInfo.html", context)  