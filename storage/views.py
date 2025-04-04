from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,authenticate
from django.contrib import messages
from django.db.models import Q
from .forms import CustomURLForm, StoredContentForm,UserProfileUpdateForm
from .models import UserSpace, StoredContent, UserProfile

from django.shortcuts import render, redirect

def landing_page(request):
    return render(request, 'landing.html') 


@login_required
def home(request):
    user_spaces = UserSpace.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CustomURLForm(request.POST)
        if form.is_valid():
            custom_url = form.cleaned_data['custom_url']

            if UserSpace.objects.filter(user=request.user, custom_url=custom_url).exists():
                messages.error(request, 'You already have a space with this custom URL.')
                return render(request, 'home.html', {
                    'form': form,
                    'user_spaces': user_spaces
                })
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
def delete_space(request, custom_url):
    user_space = get_object_or_404(UserSpace, custom_url=custom_url, user=request.user)
    if request.method == 'POST':
        user_space.delete()
        messages.success(request, f'The URL "{custom_url}" has been deleted.')
        return redirect('home')
    return redirect('home')

@login_required
def user_space(request, custom_url):
    user_space = get_object_or_404(
        UserSpace, 
        Q(custom_url=custom_url) & Q(user=request.user)
    )
    
    if request.method == 'POST':
        form = StoredContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.userspace = user_space
            content.save()
            messages.success(request, 'Content added successfully!')
            return redirect('user_space',custom_url=custom_url)
    else:
        form = StoredContentForm()
    
    contents = StoredContent.objects.filter(userspace=user_space)
    
    return render(request, 'user_space.html', {
        'user_space': user_space, 
        'contents': contents, 
        'form': form
    })

@login_required  
def public_space(request, custom_url):

    if not request.user.is_authenticated:
        return redirect('login') 

    user_space = get_object_or_404(UserSpace, custom_url=custom_url, user=request.user)
    contents = StoredContent.objects.filter(userspace=user_space)

    if request.method == 'POST':
        password = request.POST.get('password')

        user = authenticate(username=request.user.username, password=password)

        if user is None:
            messages.error(request, "Incorrect password. Please try again.")
            return render(request, 'public_space.html', {
                'userspace': user_space,
                'contents': contents,
                'error': 'Invalid password',
                'ask_for_password': True
            })
        
        return render(request, 'public_space.html', {
            'userspace': user_space,
            'contents': contents
        })

    return render(request, 'public_space.html', {
        'userspace': user_space,
        'contents': contents,
        'ask_for_password': True
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
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid(): 
            user = form.save()  
            
            if not UserProfile.objects.filter(user=user).exists():
                UserProfile.objects.create(user=user)

            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect("/") 
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "registration/signup.html", {"form": form})
    else: 
        form = UserCreationForm() 
    return render(request, "registration/signup.html", {"form": form})




@login_required
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    user_spaces = UserSpace.objects.filter(user=request.user)
    stored_contents = StoredContent.objects.filter(userspace__user=request.user)

    num_urls = user_spaces.count()
    num_contents = stored_contents.count()

    if request.method == 'POST':
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('user_profile') 
    else:
        profile_form = UserProfileUpdateForm(instance=user_profile)

    return render(request, 'profile.html', {
        'user_profile': user_profile,
        'user_spaces': user_spaces,
        'stored_contents': stored_contents,
        'num_urls': num_urls,
        'num_contents': num_contents,
        'profile_form': profile_form,
    })
