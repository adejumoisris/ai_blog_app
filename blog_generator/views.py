
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = authenticate(request, username=username, password=password )
         if user is not None:
             login(request, user)
             return redirect('/')
         else:
             error_message = "Invalid username or password "
             return render(request, 'login.html', {'error_message':error_message})

    return render(request, 'login.html')
    

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatpassword']
        # checking if the two password are correct and the same

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username,email,password)
                user.save
                # login in the user automatically without needing to loging again
                login(request,user )
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})

        else:
            error_message = 'password do not match '
            return render(request, 'signup.html', {'error_message':error_message})
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('/')
