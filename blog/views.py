# blog/views.py
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import SignUpForm
import requests
from decouple import config
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Deletes the user
        logout(request)  # Logs out the user after deletion
        messages.success(request, "Your account has been successfully deleted.")
        return redirect('index')  # Redirect to home or any other page after deletion
    return render(request, 'blog/delete_account.html')


def index(request):
    query = request.GET.get('q', 'nature')  # Default search to 'nature' if no query provided
    page = request.GET.get('page', 1)  # Get page number from request, default to 1
    
    UNSPLASH_ACCESS_KEY = config('UNSPLASH_ACCESS_KEY')
    
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    data = response.json()  # Parse the JSON response
    
    images = data.get('results', [])
    
    # For AJAX requests, return JSON response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'images': [
                {'url': img['urls']['regular'], 'alt': img.get('alt_description', 'No description')}
                for img in images
            ]
        })

    # For regular requests, render the page
    context = {
        'images': images,
        'query': query,
        'page': page
    }
    
    return render(request, 'blog/index.html', context)

# Home page view
def home(request):
    return render(request, 'blog/home.html')

# About page view
def about(request):
    return render(request, 'blog/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('index')  # Redirect to the homepage after signup
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def download_image(request):
    image_url = request.GET.get('image_url')
    response = requests.get(image_url)
    return HttpResponse(response.content, content_type="image/jpeg")

def logout_view(request):
    logout(request)
    return redirect('/')
