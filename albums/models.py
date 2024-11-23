from django.db import models
from profiles.models import Profile

class Album(models.Model):
    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ]

    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    price = models.FloatField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name
