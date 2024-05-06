from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        repeatPass = request.POST['repeatpassword']

        if password == repeatPass:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html',{'error_message': error_message})
    return  render(request, 'signup.html')


def logout_view(request):
    pass
