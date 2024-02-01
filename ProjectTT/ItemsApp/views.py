import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .forms import FormProductCreate, FormSearch
from .models import ModelProduct


# Create your views here.

def viewProductCreate(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3

    initial_data = {
        'release_date': datetime.date.today(),
    }

    # formRetrieved = rFormProductCreate() #Initialize raw django form
    # if request.method == "POST":
    #     formRetrieved = rFormProductCreate(request.POST)
    #     if formRetrieved.is_valid():    #If information provided by the user in the fields of the form pass django's validation tests, do the following:
    #         ModelProduct.objects.create(**formRetrieved.cleaned_data)   #Create new object in ModelProduct from the cleaned data that was passed from the form's fields
    #                                                                     #Using ** in front of "formRetrieved.cleaned_data" to turn the dict data into arguments for django 
    #                                                                     #to pass into the DB entry.
    #         formRetrieved = rFormProductCreate() #Re-render the form to empty the fields after saving the new product.
    
    # Simplified version of code above, using the forms.ModelForm instead of a raw forms.Form
    formRetrieved = FormProductCreate(request.POST or None, initial=initial_data) #Current date as "initial_data" for the "release_date" field
    if formRetrieved.is_valid():
        formRetrieved.save()
        formRetrieved = FormProductCreate() 

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
    
    objRetrieved = ModelProduct.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

    context = {
        "dingus": userAndArgsInfo,
        "keyObj": objRetrieved,
    }

    return render(request, "ItemsApp/productInfo.html", context)

def viewProductSearch(request, *args, **kwargs): ##### WIP - Currently working on
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
    q = request.GET.get('qT')

    if q:
        vectorSet = SearchVector('name', 'category', 'description', 'manufacturer')
        outQuery = SearchQuery(q)

        objSet = ModelProduct.objects.annotate(rank=SearchRank(vectorSet, outQuery)).order_by('-rank')
    else:
        objSet = None

    context = {
        "dingus": userAndArgsInfo,
        "results": objSet,
    }

    return render(request, "test.html", context)