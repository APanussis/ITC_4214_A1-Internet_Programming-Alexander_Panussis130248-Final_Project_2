import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

#from .forms import FormUserCreate
from .models import ModelUser

# Create your views here.

# def viewCreateUser(request, *args, **kwargs): # COULD BE DEPRECATED/COMBINED WITH viewAuthentication
#     currentUser = str(request.user)
#     flagAuthenticated = str(request.user.is_authenticated)
#     s2 = str(args)
#     s3 = str(kwargs)
#     userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
#     #objRetrieved = ModelUser.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

#     context = {
#         "currentUser": currentUser,
#         "flagAuthenticated": flagAuthenticated,
#         "dingus": userAndArgsInfo,
#         "keyObj": objRetrieved,
#     }

#     return render(request, "UsersApp/signup.html", context)

# def viewLogin(request, *args, **kwargs):
#     currentUser = str(request.user)
#     flagAuthenticated = str(request.user.is_authenticated)
#     s2 = str(args)
#     s3 = str(kwargs)
#     userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
#     #objRetrieved = ModelUser.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

#     context = {
#         "currentUser": currentUser,
#         "flagAuthenticated": flagAuthenticated,
#         "dingus": userAndArgsInfo,
#         #"keyObj": objRetrieved,
#     }

#     return render(request, "UsersApp/login.html", context)

def viewProfile(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
    #objRetrieved = ModelUser.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

    context = {
        "currentUser": currentUser,
        "flagAuthenticated": flagAuthenticated,
        "dingus": userAndArgsInfo,
        #"keyObj": objRetrieved,
    }

    return render(request, "UsersApp/userProfile.html", context)

def viewProfileList(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
    #objRetrieved = ModelUser.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

    context = {
        "currentUser": currentUser,
        "flagAuthenticated": flagAuthenticated,
        "dingus": userAndArgsInfo,
        #"keyObj": objRetrieved,
    }

    return render(request, "UsersApp/profileList.html", context)