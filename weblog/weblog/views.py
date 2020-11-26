from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse('Welcome to our Weblog!');
    return render(request,'Home.html')
def about(request):
    # return HttpResponse('About is a Hello World!');
    return render(request,'about.html')
