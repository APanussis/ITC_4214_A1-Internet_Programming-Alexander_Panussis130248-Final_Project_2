import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormLogin, FormSignup
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

#from .forms import FormUserCreate

# Create your views here.


def viewCustomLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) #Run django's built-in "authenticate" method
        if user is None: #If username or password does not match an existing registered user, throw error "errorInvalidUorP".
            context = {
                "errorInvalidUorP": "Invalid username or password."
            }
            return render(request, 'UsersApp/login.html', context)
        login(request,user)
        return render(request, 'ItemsApp/home.html') #cant use 'return redirect' within the view method, use 'request' instead
    return render(request, 'UsersApp/login.html', {})

def viewCustomLogout(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'ItemsApp/home.html') #cant use 'return redirect' within the view method, use 'request' instead
    return render(request, 'UsersApp/logout.html', {})

def viewCustomSignup(request):
    return render(request, 'UsersApp/signup.html', {})

@login_required
def viewProfile(request):
    context = {
    }
    return render(request, "UsersApp/profile.html", context)    

@login_required
def viewProfileList(request, *args, **kwargs):
    currentUser = str(request.user)
    flagAuthenticated = str(request.user.is_authenticated)
    s2 = str(args)
    s3 = str(kwargs)
    userAndArgsInfo = "User: " + currentUser + " || Authenticated: " + flagAuthenticated + " || Args: " + s2 + " || Keyword Args: " + s3
    
    #objRetrieved = ModelCHANGEtHIS.objects.get(name="1st product") #get users query info from searchbar, keywords, radiobutton filters, e.t.c.

    context = {
        "currentUser": currentUser,
        "flagAuthenticated": flagAuthenticated,
        "sessionInfo": userAndArgsInfo,
        #"keyObj": objRetrieved,
    }

    return render(request, "UsersApp/profileList.html", context)


#                                ╔═════════════════════════════════╗
# ═══════════════════════════════╣ Unused/Deprecated Code Snippets ╠═══════════════════════════════
#                                ╚═════════════════════════════════╝
#
#╔══════════════════╗
#╣ CODE SNIPPET(1*) ╠
#╚══════════════════╝
# class cViewSignup(CreateView):
#     #form_class = UserCreationForm #django's built-in creation form.
#     form_class = FormSignup #My custom sign-up form
    
#     success_url = reverse_lazy('home')  #Redirect to this URL if the form is successfully accepted.
#                                         #'reverse_lazy' is a fast implementation of the 'reverse' function, which takes the URL name as input and returns the actual URL.
#                                         #We use 'reverse_lazy' here since we are using a 'class view' instead of a 'function view', since the URLS are not loaded 
#                                         #when the files are imported.
#     template_name = "UsersApp/signup.html"

#╔══════════════════╗
#╣ CODE SNIPPET(2*) ╠
#╚══════════════════╝   
# def viewCustomLogin(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # form = FormLogin(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#     return render(request, 'UsersApp/login.html', {'form': form})


#╔══════════════════╗
#╣ CODE SNIPPET(3*) ╠
#╚══════════════════╝
# def sendOTP(email):

#     otp = None
    
#     # send random otp to email
#     otp = random.randint(100000, 999999)
#     subject = 'RPi Security System OTP'
#     message = 'Your OTP is ' + str(otp) + '. Please enter this OTP to login to your account.'
#     from_email = 'example@example.com'
#     recipient_list = [f'{email}']
    
#     send_mail(subject, message, from_email, recipient_list)

#     return otp

#╔══════════════════╗
#╣ CODE SNIPPET(4*) ╠
#╚══════════════════╝
# def viewCustomLogin(request):
#     if request.method == "POST":
#         form = FormLogin(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 email = user.email

#                 # Store user ID in session, not the user object
#                 request.session['user_id'] = user.id

#                 otp = sendOTP(email)
#                 request.session['otp_original'] = otp
#                 return redirect("success_page")  # Redirect to a success page or wherever needed
#             else:
#                 messages.error(request, 'Invalid username or password')
#         else:
#             messages.error(request, 'Invalid form input')

#     else:
#         form = FormLogin()
        
#     return render(request, 'UsersApp/login.html', {'form': form})


#╔══════════════════╗
#╣ CODE SNIPPET(5*) ╠
#╚══════════════════╝
# def viewCustomLogout(request):
#     if request.method == "POST":
#         form = FormLogin(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 email = user.email

#                 # Store user ID in session, not the user object
#                 request.session['user_id'] = user.id

#                 otp = sendOTP(email)
#                 request.session['otp_original'] = otp
#                 return redirect("success_page")  # Redirect to a success page or wherever needed
#             else:
#                 messages.error(request, 'Invalid username or password')
#         else:
#             messages.error(request, 'Invalid form input')

#     else:
#         form = FormLogin()
        
#     return render(request, 'UsersApp/login.html', {'form': form})