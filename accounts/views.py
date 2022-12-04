from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
#from django.views import generic


# Create your views here.

#class RegisterView(generic.ListView):
 #   template_name = 'college/index.html'

def register(request):
    return render(request, 'register.html')
    if request.method == 'POST':
        print('top') # We run into the issue after this line.
        first_name = request.POST['first_name']
        print('after first name')

        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Confirm passwords match and username or email isn't in use by another accout.
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('That username is already taken!')
            elif User.objects.filter(email=email).exists():
                print('That email is linked to another account!')
            else:
                # We use the predefined User table (that comes with ever Django app) to define a user here. By default, they don't have admin access.
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('New user successfully created.')
                return redirect('/')
        else:
            print("You're passwords don't match!")

    else:
        return render(request, 'college/register.html')