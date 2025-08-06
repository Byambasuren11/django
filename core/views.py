from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Хэрэглэгч үүсгэх API
@api_view(['GET'])
def create_user(request):
    user = User.objects.create_user(username='test', password='pass1234')
    return Response({'message': 'Хэрэглэгч амжилттай үүслээ'})

# Хэрэглэгч байгаа эсэхийг шалгах API
@api_view(['GET'])
def check_user(request):
    username = request.GET.get('username', '')
    exists = User.objects.filter(username=username).exists()
    return Response({
        'message': 'Hello from Django!',
        'username': username,
        'exists': exists
    })

# Энгийн HTML бүртгэлийн form үзүүлэх view
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

# Энгийн тест API
@api_view(['GET'])
def test_api(request):
    return Response({'message': 'Hello from Django!'})
