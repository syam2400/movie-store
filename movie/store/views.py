from django.shortcuts import render, redirect
from store.models import Movies
from store.forms import movieform
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


# def home(request):
#     m = Movies.objects.all()
#     return render(request, 'home.html', {'m': m})

class movielistview(ListView):
    model = Movies
    template_name = "home.html"
    context_object_name = "m"


# def add_movie(request):
#     if (request.method == "POST"):
#         n = request.POST['n']
#         d = request.POST['d']
#         y = request.POST['y']
#         i = request.FILES['i']
#         m = Movies.objects.create(name=n, desc=d, year=y, image=i)
#         m.save()
#         return redirect("/")
#     return render(request, 'add_movie.html')

class createview(CreateView):
    model = Movies
    template_name = 'add_movie.html'
    fields = ['name', 'desc', 'year', 'image']
    success_url = reverse_lazy('store:home')


# def view_movie(request, p):
#     m = Movies.objects.get(id=p)
#     return render(request, 'view_movie.html', {'k': m})

class detailview(DetailView):
    model = Movies
    template_name = 'view_movie.html'
    context_object_name = 'k'


def update_movie(request):
    f = movieform()
    if (request.method == 'POST'):
        f = movieform(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return home(request)
    return render(request, 'update.html', {'f': f})


def edit_movie(request, k):
    m = Movies.objects.get(id=k)
    f = movieform(instance=m)
    if (request.method == "POST"):
        f = movieform(request.POST, request.FILES, instance=m)
        if f.is_valid():
            f.save()
            return redirect("/")
    return render(request, 'update.html', {'f': f})


# def delete_movie(request, k):
#     if(request.method=='POST'):
#         m = Movies.objects.get(id=k)
#         m.delete()
#         return redirect("/")
#     return render(request,'delete.html')

class delete(DeleteView):
    model = Movies
    template_name = "delete.html"
    success_url = reverse_lazy('store:home')


#
# def update_movie(request):
#     f = movieform(request.POST, request.FILES)
#     if (request.method == 'POST'):
#         f = bookform(request.POST, request.FILES)
#         if f.is_valid():
#             f.save()
#             return home(request)
#     return render(request, 'update.html', {'f': f})

class update(UpdateView):
    model = Movies
    template_name = "update.html"
    fields = ['name', 'desc', 'year', 'image']
    success_url = reverse_lazy('store:home')

    # f = movieform()
    # if(request.method=='POST'):
    #     f = moiveform(request.POST)
    #     if f.is_valid():
    #         f.save()
    #         return home(request)
    # return render(request,'add_movie.html',{'f':f})
