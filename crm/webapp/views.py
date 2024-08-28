from django.shortcuts import render, redirect
# Create your views here.

from .forms import CreateUserForm, LoginUserForm, CreateClientForm, UpdateClientForm
from .models import Client

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'webapp/index.html')



# register a user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # posts the data
            # redirect to another page
            return redirect('login')

    # the form contains our username, pasword 
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)

# login a user
def login_user(request):
    form = LoginUserForm()

    if request.method == "POST":
        form = LoginUserForm(request=request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)


def logout_user(request):
    auth.logout(request)
    return redirect('login')


# dashboard view
@login_required(login_url='login') # ensures logged in to access dashboard, else redirect to login page
def dashboard(request):
    # passes through all client model objects to dashboard rendering
    clients = Client.objects.all()

    # 'clients' is key used in dashboard.html
    context = {'clients': clients}

    return render(request, 'webapp/dashboard.html', context=context)


# add records
@login_required(login_url='login') # ensures logged in to access dashboard, else redirect to login page
def create_horse(request):
    
    form = CreateClientForm()

    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save() # posts the data
            # redirect to another page
            return redirect('dashboard')

    # the form contains our username, pasword 
    context = {'form': form}
    return render(request, 'webapp/create-horse.html', context=context) 

# update record
@login_required(login_url='login') # ensures logged in to access dashboard, else redirect to login page
def update_horse(request, pk):
    
    # gets info of specific client (w/ id pk), all collected into one data object
    horse_info = Client.objects.get(id=pk)

    form = UpdateClientForm(instance=horse_info)

    # when updating the client's form
    if request.method == 'POST':
        # adds whatever is updated to the form
        form = UpdateClientForm(request.POST, instance=horse_info)
        if form.is_valid():
            form.save() # posts the data
            # redirect to another page
            return redirect('dashboard')

    # the form contains our username, pasword 
    context = {'form': form}
    return render(request, 'webapp/update-horse.html', context=context) 



# read or view a horse
@login_required(login_url='login') # ensures logged in to access dashboard, else redirect to login page
def view_horse(request, pk):
    
    horse_info = Client.objects.get(id=pk)
    context = {'horse': horse_info}

    return render(request, 'webapp/view-horse.html', context=context)


# delete horse
@login_required(login_url='login') # ensures logged in to access dashboard, else redirect to login page
def delete_horse(request, pk):
    
    horse_info = Client.objects.get(id=pk)
    horse_info.delete()
    return redirect('dashboard')
