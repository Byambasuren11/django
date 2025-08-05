from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import render, redirect

def create_user(request):
    user = User.objects.create_user(username='test', password='pass1234')
    return JsonResponse({'message': 'Хэрэглэгч амжилттай үүслээ'})

def check_user(request):
    username = request.GET.get('username', '')
    exists = User.objects.filter(username=username).exists()
    return JsonResponse({'exists': exists})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Хэрэглэгчийн нэр аль хэдийн байна!")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return HttpResponse("Амжилттай бүртгэгдлээ!")

    return render(request, 'signup.html')

