from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,authenticate
from django.contrib import messages
from django.db.models import Q
from .models import UserSpace, StoredContent
from .forms import CustomURLForm, StoredContentForm

@login_required
def home(request):
    user_spaces = UserSpace.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CustomURLForm(request.POST)
        if form.is_valid():
            # Check if custom URL already exists
            custom_url = form.cleaned_data['custom_url']
            
            # Check if URL is already taken
            if UserSpace.objects.filter(custom_url=custom_url).exists():
                messages.error(request, 'This custom URL is already taken. Please choose another.')
                return render(request, 'home.html', {
                    'form': form, 
                    'user_spaces': user_spaces
                })
            
            # Create new user space
            user_space = form.save(commit=False)
            user_space.user = request.user
            user_space.save()
            
            messages.success(request, 'Custom URL created successfully!')
            return redirect('user_space', custom_url=custom_url)
    else:
        form = CustomURLForm()
    
    return render(request, 'home.html', {
        'form': form, 
        'user_spaces': user_spaces
    })

@login_required
def user_space(request, custom_url):
    # Get the UserSpace or return 404
    user_space = get_object_or_404(
        UserSpace, 
        Q(custom_url=custom_url) & Q(user=request.user)
    )
    
    # Handle content addition
    if request.method == 'POST':
        form = StoredContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.userspace = user_space
            content.save()
            messages.success(request, 'Content added successfully!')
            return redirect('user_space', custom_url=custom_url)
    else:
        form = StoredContentForm()
    
    # Get stored contents for this space
    contents = StoredContent.objects.filter(userspace=user_space)
    
    return render(request, 'user_space.html', {
        'user_space': user_space, 
        'contents': contents, 
        'form': form
    })

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import UserSpace, StoredContent
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import UserSpace, StoredContent

def public_space(request, custom_url):
    # View for public access to user space
    user_space = get_object_or_404(UserSpace, custom_url=custom_url)
    contents = StoredContent.objects.filter(userspace=user_space)

    if request.method == 'POST':
        # Check for password confirmation
        password = request.POST.get('password')
        
        # Authenticate with the logged-in user
        user = authenticate(username=request.user.username, password=password)
        
        if user is None:
            # Invalid password
            messages.error(request, "Incorrect password. Please try again.")
            return render(request, 'public_space.html', {
                'userspace': user_space, 
                'contents': contents, 
                'error': 'Invalid password',
                'ask_for_password': True  # Flag to show password prompt
            })
        
        # If password is correct, proceed
        return render(request, 'public_space.html', {
            'userspace': user_space, 
            'contents': contents
        })
    
    return render(request, 'public_space.html', {
        'userspace': user_space, 
        'contents': contents,
        'ask_for_password': True  # Flag to show password prompt
    })

    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')
    
def authview(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user) 
            messages.success(request, "Registration successful!")
            return redirect("/")
        else:
            # If form is not valid, pass the form with errors back to the template
            messages.error(request, "Please correct the errors below.")
            return render(request, "registration/signup.html", {"form": form})
    else: 
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})



# <h1>{{ userspace.user.username }}'s Space</h1>

# {% for content in contents %}

# {% endfor %}