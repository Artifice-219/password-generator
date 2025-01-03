from django.shortcuts import render
from django.http import JsonResponse
import string, random

# Create your views here.
def index(request):
    return render(request, 'index.html')

# this is the part where you should generate a random password
def get_password(request):
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    special_chars = list(string.punctuation)

    pool = uppercase + lowercase + special_chars
    password = ''.join(random.choice(pool) for _ in range(14))

    return JsonResponse({
        'password' : password
    })
