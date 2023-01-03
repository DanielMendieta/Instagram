from django.shortcuts import render

def register(request):
   return render(request, 'accounts/register.html')

def login_user(request):
   return render(request, 'accounts/login.html')   