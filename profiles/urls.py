from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('profile/details/', views.profile_details, name='profile_details'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]
