import datetime
import time

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import FormProduct, FormSearch
from .models import ModelProduct

# Create your views here.

#                                 ╔════════════════════════════════════════════════╗
# ╔═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╣ THE VIEW bellow ONLY FOR TESTING AND DEBUGGING ╠═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╗
# ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ╚════════════════════════════════════════════════╝ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║

@login_required
def viewTest(request, *args, **kwargs): ##### WIP - Currently working on
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    q = request.GET.get('qT')
    if q:
        vectorSet = SearchVector('name', 'category', 'description', 'manufacturer')
        outQuery = SearchQuery(q)

        #Grab objects from ModelProduct, 
        # who's data matches with the string provided in the search form inside the template, 
        # prioritizing 'name', 'category', 'description'and lastly 'manufacturer' as the data used to make the order in which they are displayed,
        # filter out and remove any results that have a rank score GREATER THAN or EQUAL to 0.001,
        # and then order the results by their final rank score.
        objSet = ModelProduct.objects.annotate(rank=SearchRank(vectorSet, outQuery)).filter(rank__gte=0.001).order_by('-rank')
    else:
        objSet = None

    context = {
        "currentUser": currentUser,
        "flagAuthenticated": flagAuthenticated,
        "sessionInfo": userAndArgsInfo,
        "results": objSet,
    }

    return render(request, "test.html", context)

# ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ╔═══════════════════════════════════════════════╗ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║
# ╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╣ THE VIEW above ONLY FOR TESTING AND DEBUGGING ╠═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝
#                                 ╚═══════════════════════════════════════════════╝

def viewProductSearch(request): 
    q = request.GET.get('qT')
    if q:
        vectorSet = SearchVector('name', 'category', 'description', 'manufacturer')
        outQuery = SearchQuery(q)

        #Grab objects from ModelProduct, 
        # who's data matches with the string provided in the search form inside the template, 
        # prioritizing 'name', 'category', 'description'and lastly 'manufacturer' as the data used to make the order in which they are displayed,
        # filter out and remove any results that have a rank score GREATER THAN or EQUAL to 0.001,
        # and then order the results by their final rank score.
        objSet = ModelProduct.objects.annotate(rank=SearchRank(vectorSet, outQuery)).filter(rank__gte=0.001).order_by('-rank')
    else:
        objSet = None

    context = {
        "results": objSet,
    }
    return render(request, "ItemsApp/home.html", context)

@login_required
def viewProductCreate(request): #FIX IMAGES NOT GETTING SAVED IN SEPERATE DIRS
    
    initial_data = {
        'release_date': datetime.date.today(),
    }
        
    # Simplified version of CODE SNIPPET(1*), using the forms.ModelForm instead of a raw forms.Form
    formRetrieved = FormProduct(request.POST or None, request.FILES or None, initial=initial_data) #Current date as "initial_data" for the "release_date" field
    if formRetrieved.is_valid():
        formRetrieved.save()
        formRetrieved = FormProduct()
    context = {
        "keyForm": formRetrieved,
    }
    return render(request, "ItemsApp/productCreate.html", context)

def viewProductInfo(request, id): #View with 'Dynamic Lookup' functionality where the "id" of an entry in the model "ModelProduct" gets passed as an argument "arg_id".
    objRetrieved = None
    if id is not None:
        objRetrieved = ModelProduct.objects.get(id=id)

    context = {
        "keyObj": objRetrieved,
    }

    return render(request, "ItemsApp/productInfo.html", context)

@login_required
def viewProductEdit(request, id):
    objRetrieved = None

    if id is not None:
        objRetrieved = ModelProduct.objects.get(id=id)
        

    print(objRetrieved.id, objRetrieved.name)
    formRetrieved = FormProduct(request.POST or None, request.FILES or None, instance=objRetrieved) #Current date as "initial_data" for the "release_date" field
    if formRetrieved.is_valid():
        formRetrieved.save()
        #formRetrieved = FormProduct(request.POST or None, request.FILES or None, instance=objRetrieved)
        return render(request, "ItemsApp/productInfo.html", {"keyObj": objRetrieved})
    
    context = {
        "keyObj": objRetrieved,
        "keyForm": formRetrieved,
    }
    return render(request, "ItemsApp/productEdit.html", context)

### WIP
@login_required
def viewProductDelete(request, id):
    objRetrieved = None
    if id is not None:
        objRetrieved = ModelProduct.objects.get(id=id)
        if request.method == "POST":
            objRetrieved.delete()
            return HttpResponseRedirect(reverse("home"))

    context = {
        "keyObj": objRetrieved,
    }
    return render(request, "ItemsApp/productDelete.html", context)

#                                ╔═════════════════════════════════╗
# ═══════════════════════════════╣ Unused/Deprecated Code Snippets ╠═══════════════════════════════
#                                ╚═════════════════════════════════╝
#
#╔══════════════════╗
#╣ CODE SNIPPET(1*) ╠
#╚══════════════════╝
# formRetrieved = rFormProductCreate() #Initialize raw django form
# if request.method == "POST":
#     formRetrieved = rFormProductCreate(request.POST)
#     if formRetrieved.is_valid():    #If information provided by the user in the fields of the form pass django's validation tests, do the following:
#         ModelProduct.objects.create(**formRetrieved.cleaned_data)   #Create new object in ModelProduct from the cleaned data that was passed from the form's fields
#                                                                     #Using ** in front of "formRetrieved.cleaned_data" to turn the dict data into arguments for django 
#                                                                     #to pass into the DB entry.
#         formRetrieved = rFormProductCreate() #Re-render the form to empty the fields after saving the new product.

#╔══════════════════╗
#╣ CODE SNIPPET(2*) ╠
#╚══════════════════╝
# def viewProductInfo(request, TT_arg_id): #View with 'Dynamic Lookup' functionality where the "id" of an entry in the model "ModelProduct" gets passed as an argument "arg_id".
#     objRetrieved = ModelProduct.objects.get(id=TT_arg_id) # MAKE THIS WORK DYNAMICALLY
#     context = {
#         "keyObj": objRetrieved,
#     }
#     return render(request, "ItemsApp/productInfo.html", context)

#╔══════════════════╗
#╣ CODE SNIPPET(3*) ╠
#╚══════════════════╝
# initial_data = {
        #     'name': objRetrieved.name,
        #     'image': objRetrieved.image ,
        #     'description': objRetrieved.description,
        #     'category':objRetrieved.category,
        #     'release_date': objRetrieved.release_date,
        #     'current_stock': objRetrieved.current_stock,
        #     'manufacturer': objRetrieved.manufacturer,
        #     'price': objRetrieved.price ,
        #     'featured_status': objRetrieved.featured_status ,
        #     'featured_promo_overlay': objRetrieved.featured_promo_overlay,
        # }
#     else:
#         validationF = "INVALID or MISSING critical information. Check your fields."
#         context = {
#             "validationFlag": validationF,
#             "keyForm": formRetrieved,
#             "keyObj": objRetrieved,
#         }
#         return render(request, "ItemsApp/productEdit.html", context)

# else:
#     objRetrieved = ModelProduct.objects.get()
#     validationF = "Product does not exist, or just got removed. Redirecting to Create page..."
#     context = {
#         "validationFlag": validationF,
#         "keyForm": formRetrieved,
#         "keyObj": objRetrieved,
#     }
#     return render(request, "ItemsApp/productEdit.html", context)
#     time.sleep(5)
#     return HttpResponseRedirect("ItemsApp/productCreate.html")

# context = {
#     "validationFlag": validationF,
#     "keyForm": formRetrieved,
#     "keyObj": objRetrieved,
# }
# return render(request, "ItemsApp/productEdit.html", context)