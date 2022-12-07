from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth # User: send the data back to the User table. auth: Needed for logging in.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
    
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials.')
            return HttpResponseRedirect(request.path_info)

    else:
        return render(request, 'college/register.html')

def register(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Confirm passwords match and username or email isn't in use by another accout.
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('That username is already taken!')
                messages.info(request, 'That username is already taken!')
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(email=email).exists():
                print('That email is linked to an existing account!')
                messages.info(request, 'That email is linked to an existing account!')
                return HttpResponseRedirect(request.path_info)
            else:
                # We use the predefined User table (that comes with ever Django app) to define a user here. create_user doesn't give admin access.
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('New user successfully created.')
                messages.info(request, 'New user successfully created.')
                return render(request, 'college/login.html')
        else:
            print("The passwords don't match!")
            messages.info(request, "The passwords don't match!")
            return HttpResponseRedirect(request.path_info)

    else:
        return render(request, 'college/register.html')

def logout(request):
    auth.logout(request)
    return render(request, 'college/register.html')