from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from albums.models import Album

def home(request):
    profile = Profile.objects.first()
    if profile:
        albums = Album.objects.filter(owner=profile)
        return render(request, 'profiles/home-with-profile.html', {'profile': profile, 'albums': albums})
    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = ProfileForm()
        return render(request, 'profiles/home-no-profile.html', {'form': form})

def profile_details(request):
    profile = Profile.objects.first()
    if profile:
        albums_count = Album.objects.filter(owner=profile).count()
        return render(request, 'profiles/profile_details.html', {'profile': profile, 'albums_count': albums_count})
    return redirect('/')

def delete_profile(request):
    profile = Profile.objects.first()
    if profile:
        if request.method == 'POST':
            profile.delete()
            return redirect('/')
        return render(request, 'profiles/delete_profile.html', {'profile': profile})
    return redirect('/')
