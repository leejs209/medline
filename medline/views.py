from django.shortcuts import render

def home(request):
    name = '홈'
    userid = request.user.id

    return render(request, 'medline/home.html', {'userid': userid, 'title': name})

def contact(request):
    name = '연락'
    userid = request.user.id

    return render(request, 'medline/contact.html', {'userid': userid, 'title': name})

def consultform(request):
    name = '상담신청'
    userid = request.user.id

    return render(request, 'medline/consultform.html', {'userid': userid, 'title': name})

def login(request):
    name = '로그인'
    userid = request.user.id

    return render(request, 'medline/../templates/registration/login.html', {'userid': userid, 'title': name})