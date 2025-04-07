from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Item


# this is a view to what page opens when the website is first visited
def home(request):
    return render(request, 'store/home.html', {})

# This is for the home button on base.html to work
def homepage(request):
    return render(request, 'store/home.html', {})

# Login view
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login, username or password is not registered')
            return redirect('login')

    else:
        return render(request, 'store/login.html')

# Logout view
def logout(request):
    auth.logout(request)
    return redirect('/')

# User registration view
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(email=email).exists(): # checks for existing email
                messages.info(request, 'Email is already in use.')
                return redirect('register')  #redirects the page back to register.html with message
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already in use.')
                return redirect('register')
            else:
                #This saves a user in the database
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, email=email, password=password, username=username
                )
                user.save()
                messages.info(request, 'Account created successfully.')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
    return render(request, 'store/register.html')

# Store page with optional search
def store_page(request):
    query = request.GET.get('q')
    if query:
        items = Item.objects.filter(title__icontains=query)
    else:
        items = Item.objects.all()
    return render(request, 'store/store_page.html', {'items': items})

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'store/item_detail.html', {'item': item})