from django.shortcuts import render
from store.models import Movies
# Create your views here.
from django.http import HttpResponse

def home(request):

    return render(request,'home.html')
def index(request):
    return render(request,'index.html')



    #lkfvkfjjsjvsjv;sdjv;oskv;odskv;sjhbj