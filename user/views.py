from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render




# Create your views here.
def loginUser(request):
   
    
    return render(request, "login_page.html")

