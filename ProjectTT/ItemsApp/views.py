from django.http import HttpResponse
from django.shortcuts import render

from .forms import FormProductCreate, rFormProductCreate
from .models import ModelProduct


# Create your views here.

def viewProductCreate(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3

    formRetrieved = rFormProductCreate() #Initialize raw django form
    if request.method == "POST":
        formRetrieved = rFormProductCreate(request.POST)
        if formRetrieved.is_valid():    #If information provided by the user in the fields of the form pass django's validation tests, do the following:
            ModelProduct.objects.create(**formRetrieved.cleaned_data)   #Create new object in ModelProduct from the cleaned data that was passed from the form's fields
                                                                        #Using ** in front of "formRetrieved.cleaned_data" to turn the dict data into arguments for django 
                                                                        #to pass into the DB entry.
            formRetrieved = rFormProductCreate() #Re-render empty form
            
    
    # formRetrieved = FormProductCreate(request.POST or None)
    # if formRetrieved.is_valid():
    #     formRetrieved.save()
    #     formRetrieved = FormProductCreate() #Re-render the form to empty the fields after saving the new product.

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