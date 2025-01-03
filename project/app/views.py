from django.shortcuts import render
from django.http import JsonResponse
import string

# Create your views here.
def index(request):
    return render(request, 'index.html')

# this is the part where you should generate a random password
def get_password(request):
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_uppercase)
    special_chars = list(string.punctuation)
    password = 'this youre password you piece of shit'

    return JsonResponse({
        'password' : password
    })
