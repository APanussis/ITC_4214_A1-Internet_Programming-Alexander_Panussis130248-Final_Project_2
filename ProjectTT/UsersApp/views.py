import datetime
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import transaction

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .models import ModelProfile
from .forms import FormLogin, FormSignup, FormUser, FormProfile
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# Create your views here.

#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: signup.html                                                                                                                                           ║
#║ Implements model: auth.User                                                                                                                                                    ║
#║ Implements form: auth.forms.UserCreationForm                                                                                                                                   ║
#║ Permissions required: NONE                                                                                                                                                     ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with a basic registration form which is built-in to the "django.contrib.auth" package. If user input is valid, they become registered with                 ║
#║ the credentials they provided and are added as an entry to django's default "User" model and are then redirected back to "login.html" page.                                    ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def viewCustomSignup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        userObj = form.save()
        return HttpResponseRedirect(reverse("login"))
    return render(request, 'UsersApp/signup.html', {"keyForm": form})


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: login.html                                                                                                                                            ║
#║ Implements model: auth.User                                                                                                                                                    ║
#║ Implements form: auth.forms.AuthenticationForm                                                                                                                                 ║
#║ Permissions required: NONE                                                                                                                                                     ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with a basic login form which is built-in to the "django.contrib.auth" package. If user input is valid and passes they authentication process, they        ║
#║ are logged in and can now continue browsing the website with greater permissions, as long as they do not end their current browser session. If the user tries to access        ║
#║ the website from a different session they will be asked to go to the login page and go through the login process once more.                                                    ║
#║ If the credentials entered during the login process do not match any of the entries in the auth.User table the page is re-rendered with a message informing the user that      ║
#║ authentication was unsuccessful.                                                                                                                                               ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def viewCustomLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = AuthenticationForm(request)

    context = {
        "keyForm": form,
    }
    return render(request, 'UsersApp/login.html', context)


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: logout.html                                                                                                                                           ║
#║ Implements model: auth.User                                                                                                                                                    ║
#║ Implements form: NONE                                                                                                                                                          ║
#║ Permissions required: User needs to be logged in.                                                                                                                              ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with a form that consists of a "logout confirmation" message and button. Once the button is clicked, it runs the logout method and sends                   ║
#║ the now anonymous user to the "home.html" page.                                                                                                                                ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
@login_required
def viewCustomLogout(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'ItemsApp/home.html') #cant use 'return redirect' within the view method, use 'request' instead
    return render(request, 'UsersApp/logout.html', {})



#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: profile.html                                                                                                                                          ║
#║ Implements model: auth.User, ModelProfile(OneToOne: User.id)                                                                                                                   ║
#║ Implements form: NONE                                                                                                                                                          ║
#║ Permissions required: User needs to be logged in.                                                                                                                              ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Attempts to get the current user. If the user is authenticated, links will appear on the navbar(permissions: @login_required) linking to the "profile.html" page.         ║
#║ Once the profile picture or the button with the user's username is clicked, a request tries gets the current users id. If it exists as an entry in the auth.User model, it     ║
#║ renders a page with the currently signed-in user's profile information.                                                                                                        ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
@login_required
def viewProfile(request):
    currentUserId = str(request.user.id)
    if id is not None:
        userRetrieved = User.objects.get(id=currentUserId)

    context = {
        "keyObj": userRetrieved,
    }
    return render(request, "UsersApp/profile.html", context)


#╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║ Implemented in Template: profileEdit.html                                                                                                                                      ║
#║ Implements model: auth.User, ModelProfile(OneToOne: User.id)                                                                                                                   ║
#║ Implements form: FormUser, FormProfile                                                                                                                                         ║
#║ Permissions required: User needs to be logged in.                                                                                                                              ║
#║                                                                                                                                                                                ║
#║ Description:                                                                                                                                                                   ║
#║      Renders a page with TWO(2) forms with their fields populated with the current user's data from the "auth.User" and the "ModelProfile" tables. The user then has the       ║
#║ option to add or change their information and profile picture. If the new information they provide is valid and they click "Save", the changes are saved and they are sent     ║
#║ back tothe "profile.html" page. The "Back to Profile" button simply sends the user back to "profile.html" page WITHOUT saving any changes made.                                ║
#╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
@login_required
def viewProfileEdit(request): #same funct as viewProductEdit
    currentUserId = str(request.user.id)
    if id is not None:
        userRetrieved = User.objects.get(id=currentUserId)
        profileRetrieved = ModelProfile.objects.get(id=currentUserId)

    formRetrievedUser = FormUser(request.POST or None, request.FILES or None, instance=userRetrieved)
    formRetrievedProfile = FormProfile(request.POST or None, request.FILES or None, instance=profileRetrieved)

    if formRetrievedUser.is_valid() and formRetrievedProfile.is_valid():
        formRetrievedUser.save()
        formRetrievedProfile.save()
        return render(request, "UsersApp/profile.html", {"keyObj": userRetrieved})
    
    context = {
        "keyObj": userRetrieved,
        "keyFormUser": formRetrievedUser,
        "keyFormProfile": formRetrievedProfile,
    }
    return render(request, "UsersApp/profileEdit.html", context)


#                                ╔════════════════════╗
# ═══════════════════════════════╣ Unimplemented Code ╠═══════════════════════════════
#                                ╚════════════════════╝
# @login_required
# def viewProfileList(request, *args, **kwargs):
#     currentUser = str(request.user)
#     flagAuthenticated = str(request.user.is_authenticated)
#     s2 = str(args)
#     s3 = str(kwargs)
#     userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
#     #objRetrieved = ModelCHANGEtHIS.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

#     context = {
#         "currentUser": currentUser,
#         "flagAuthenticated": flagAuthenticated,
#         "sessionInfo": userAndArgsInfo,
#         #"keyObj": objRetrieved,
#     }

#     return render(request, "UsersApp/profileList.html", context)

