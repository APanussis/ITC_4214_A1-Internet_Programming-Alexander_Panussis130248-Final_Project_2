import datetime
import time

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import FormProduct, FormCategory, FormManufacturer
from .models import ModelProduct

# Create your views here.

#                                 ╔═══════════════════════════════════════════════════════════╗
# ╔═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╣ THE VIEW bellow (viewTest) ONLY FOR TESTING AND DEBUGGING ╠═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╗
# ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ╚═══════════════════════════════════════════════════════════╝ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║

@login_required
def viewTest(request, *args, **kwargs): 
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

# ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ╔══════════════════════════════════════════════════════════╗ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║ ║
# ╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╣ THE VIEW above (viewTest) ONLY FOR TESTING AND DEBUGGING ╠═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝
#                                 ╚══════════════════════════════════════════════════════════╝




#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: home.html                                                                                                                                             ║
#║ Implements model: ModelProduct                                                                                                                                                 ║
#║ Implements form: FormSearch                                                                                                                                                    ║ 
#║ Permissions required: NONE                                                                                                                                                     ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a form for the user to put in a search term. Once the user presses the Search button, if there was any input provided in the search field, it uses the input      ║
#║ to create a postgreSQL "SearchQuery" and sends it looking down the "SearchVectors" (target table columns) provided in the view. Then it returns results from the ModelProduct  ║
#║ table that have a search ranking score greater than 0.001 and orders them from highest to lowest. Ranking score is basically a search relevance score built into postgreSQL    ║
#║ query functionality.                                                                                                                                                           ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def viewProductSearch(request): 
    q = request.GET.get('qT')
    if q:
        vectorSet = SearchVector('name', 'category', 'description', 'manufacturer')
        outQuery = SearchQuery(q)
        objSet = ModelProduct.objects.annotate(rank=SearchRank(vectorSet, outQuery)).filter(rank__gte=0.001).order_by('-rank')
    else:
        objSet = None

    context = {
        "results": objSet,
    }
    return render(request, "ItemsApp/home.html", context)


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: optionsCreate.html                                                                                                                                    ║
#║ Implements model: ModelCategory, ModelManufacturer                                                                                                                             ║
#║ Implements form: FormCategory, FormManufacturer                                                                                                                                ║
#║ Permissions required: User needs to be logged in.                                                                                                                              ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with two forms: one to create a new category entry in the ModelCategory and another for the ModelManufacturer. Once valid input is typed into a form and   ║
#║ the "Add" button is clicked, the new entry becomes available for selection during new product entry creations or editing. (See views "viewProductCreate" and                   ║
#║ "viewProductEdit" further bellow)                                                                                                                                              ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
@login_required
def viewOptionsCreate(request): 
    
    formCategoryRetrieved = FormCategory(request.POST or None)
    formManufacturerRetrieved = FormManufacturer(request.POST or None)

    if formCategoryRetrieved.is_valid():
        formCategoryRetrieved.save()
        formCategoryRetrieved = FormCategory()

    if formManufacturerRetrieved.is_valid():
        formManufacturerRetrieved.save()
        formManufacturerRetrieved = FormManufacturer()

    context = {
        "keyFormCategory": formCategoryRetrieved,
        "keyFormManufacturer": formManufacturerRetrieved,
    }
    return render(request, "ItemsApp/optionsCreate.html", context)


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: productCreate.html                                                                                                                                    ║
#║ Implements model: ModelProduct, ModelCategory(ForeignKey), ModelManufacturer(ForeignKey)                                                                                       ║
#║ Implements form: FormProduct                                                                                                                                                   ║
#║ Permissions required: User needs to be logged in.                                                                                                                              ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with a form with all the fields to create a new product entry. Initial data populates the release_date field with a date corresponding to the systems date.║
#║ If the data provided is valid the entry is saved and the page is rerendered. Otherwise validation messages popup depending on which field has an error.                        ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
@login_required
def viewProductCreate(request): 
    
    initial_data = {
        'release_date': datetime.date.today(),
    }
        
    formProductRetrieved = FormProduct(request.POST or None, request.FILES or None, initial=initial_data) 
    if formProductRetrieved.is_valid():
        formProductRetrieved.save()
        formProductRetrieved = FormProduct()

    context = {
        "keyForm": formProductRetrieved,
    }
    return render(request, "ItemsApp/productCreate.html", context)


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: productInfo.html                                                                                                                                      ║
#║ Implements model: ModelProduct, ModelCategory(ForeignKey), ModelManufacturer(ForeignKey)                                                                                       ║
#║ Implements form: NONE                                                                                                                                                          ║
#║ Permissions required: NONE                                                                                                                                                     ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with information corresponding to the product link clicked from the results that are rendered in the home.html template by the view "viewSearch".          ║
#║ The entry's information is rendered as an sql query OBJECT stored in a variable which can then be rendered to the template as an entry of a python context dictionairy.        ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def viewProductInfo(request, id): #View with 'Dynamic Lookup' functionality where the "id" of an entry in the model "ModelProduct" gets passed as an argument "arg_id".
    objRetrieved = None
    if id is not None:
        objRetrieved = ModelProduct.objects.get(id=id)

    context = {
        "keyObj": objRetrieved,
    }

    return render(request, "ItemsApp/productInfo.html", context)


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: productEdit.html                                                                                                                                      ║
#║ Implements model: ModelProduct, ModelCategory(ForeignKey), ModelManufacturer(ForeignKey)                                                                                       ║
#║ Implements form: FormProduct                                                                                                                                                   ║
#║ Permissions required: User needs to be logged in.                                                                                                                              ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with a form with all the fields to edit a product entry. The fields of the form are populated with the entry's data, which come in the form of             ║
#║ an sql OBJECT. If the data provided is valid the entry is saved and the user is redirected to the productInfo page whe the entry is now render with its update information.    ║
#║ Otherwise validation messages popup depending on which field has an error.                                                                                                     ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
@login_required 
def viewProductEdit(request, id):
    objRetrieved = None

    if id is not None:
        objRetrieved = ModelProduct.objects.get(id=id)
        

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


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: productDelete.html                                                                                                                                    ║
#║ Implements model: ModelProduct, ModelCategory(ForeignKey), ModelManufacturer(ForeignKey)                                                                                       ║
#║ Implements form: NONE                                                                                                                                                          ║
#║ Permissions required: User needs to be logged in.                                                                                                                              ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with deletion confirmation message asking the user if they are sure that they want to delete the entry that was displayed in the previously                ║
#║ rendered productInfo.html template. If the user clicks on the "Yes, Delete it" the entry is deleted and the user is redirected to the home.html template.                      ║
#║ If the user instead clicks on "No. Go back." they return to the productInfo.html template and the entry's information is re-rendered.                                          ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
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