from django.http import HttpResponse
from django.shortcuts import render

#from ShopApp.forms import FormCreateProduct, FormRawCreateProduct
#from ItemsApp.models import ModelProduct

# Create your views here.


def viewCart(request, *args, **kwargs):
    currentUser = str(request.user)
    s1 = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    printThis = "User: " + currentUser + " || Authenticated: " + s1 + " || Args: " + s2 + " || Keyword Args: " + s3
    contentGreet = "Hello " + currentUser + "."
    itemList1 = [4, 'long list', 'of items']
    itemList1F = ' | '.join(map(str, itemList1))

    context = {           
        "sessionInfo": printThis,
        "Greeting": contentGreet,
        "ExampleList1": itemList1F,
    }
    return render(request, "cart.html", context)


#                                ╔═════════════════════════════════╗
# ═══════════════════════════════╣ Unused/Deprecated Code Snippets ╠═══════════════════════════════
#                                ╚═════════════════════════════════╝
#
#╔══════════════════╗
#╣ CODE SNIPPET(1*) ╠
#╚══════════════════╝
# Currently using the VIEW in the ItemsApp instead of this one.
# def viewTest(request, *args, **kwargs):
#     currentUser = str(request.user)
#     s1 = str(request.user.is_authenticated)
#     s2 = str(args)
#     s3 = str(kwargs)
#     printThis = "User: " + currentUser + " || Authenticated: " + s1 + " || Args: " + s2 + " || Keyword Args: " + s3
#     context = {
#         "sessionInfo": printThis
#     }

#     #return HttpResponse("<h1>Sample txt. Current user is: %s </h1>" % printThis)
#     return render(request, "test.html", context)

#╔══════════════════╗
#╣ CODE SNIPPET(2*) ╠
#╚══════════════════╝
# Currently using the VIEW in the ItemsApp instead of this one.
# def viewHome(request, *args, **kwargs):
#     currentUser = str(request.user)
#     s1 = str(request.user.is_authenticated)
#     s2 = str(args)
#     s3 = str(kwargs)
#     printThis = "User: " + currentUser + " || Authenticated: " + s1 + " || Args: " + s2 + " || Keyword Args: " + s3
#     context = {
#         "sessionInfo": printThis
#     }
#     return render(request, "home.html", context)

#╔══════════════════╗
#╣ CODE SNIPPET(3*) ╠
#╚══════════════════╝
# def viewNavbar(request, *args, **kwargs): 
#     currentUser = str(request.user)
#     flagAuthenticated = str(request.user.is_authenticated)
#     s2 = str(args)
#     s3 = str(kwargs)
#     #userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
#     #objRetrieved = ModelUser.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

#     context = {
#         "currentUser": currentUser,
#         "flagAuthenticated": flagAuthenticated,
#         #"sessionInfo": userAndArgsInfo,
#         #"keyObj": objRetrieved,
#     }

#     return render(request, "/navbar.html", context)