from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
from profiles.models import Profile

def add_album(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('/')
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = profile
            album.save()
            return redirect('/')
    else:
        form = AlbumForm()
    return render(request, 'albums/album_add.html', {'form': form})

def album_details(request, id):
    album = get_object_or_404(Album, id=id)
    return render(request, 'albums/album_details.html', {'album': album})

def edit_album(request, id):
    album = get_object_or_404(Album, id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'form': form, 'album': album})

def delete_album(request, id):
    album = get_object_or_404(Album, id=id)
    if request.method == 'POST':
        album.delete()
        return redirect('/')
    return render(request, 'albums/album_delete.html', {'album': album})
