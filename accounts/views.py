from django.shortcuts import render, redirect
from django.contrib.auth.models import User# , auth # User: send the data back to the User table. auth: Needed for logging in.


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Delete this section once we fix the error.
        # ERROR that occurs trying to create the user object: IntegrityError at /accounts/register/ ---> NOT NULL constraint failed: auth_user.last_name
        # We can get past this error by removing the first_name and last_name initializations on the next line, but then
        # when a user is created and you go view it in the admin panel, only the username was saved.
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        user.save();
        print('New user successfully created.')
        return redirect('/')
        # STOP DELETING HERE. Uncomment the section below by highlighting it, and hitting CMD + K + U.

        # # Confirm passwords match and username or email isn't in use by another accout.
        # if password1 == password2:
        #     if User.objects.filter(username=username).exists():
        #         print('That username is already taken!')
        #     elif User.objects.filter(email=email).exists():
        #         print('That email is linked to another account!')
        #     else:
        #         # We use the predefined User table (that comes with ever Django app) to define a user here. create_user doesn't give admin access.
        #         user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        #         user.save();
        #         print('New user successfully created.')
        #         return redirect('/')
        # else:
        #     print("You're passwords don't match!")

    else:
        return render(request, 'college/register.html')