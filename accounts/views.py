from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

#user register
def register(request):
    if request.method == 'POST':
       #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, "email is being used")
                    return redirect('register')
                else:
                   user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                   user.save()
                   messages.success(request, 'you ar registered and can log in')
                   return redirect('login')
                   #login after register
                #    auth.login(request,user)
                #    messages.success(request,"Account create successfully! your ar logged in")
                #    return redirect('home')
                    
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

#user login
def login(request):
    if request.method == 'POST': 
        return
    else:
        return render(request, 'accounts/login.html')
    

#user logout
def logout(request):
    return redirect('Home')

#dashboard
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
