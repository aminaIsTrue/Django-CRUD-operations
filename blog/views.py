from django.shortcuts import render,redirect

from .forms import PostForm
from .models import Post
# Create your views here.


#create view
def create_view(request):

    if request.method == 'POST':

        obj = PostForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('home-path')

    return render(request, 'blog/create.html', {'form' : PostForm()})


#list view

def list_view(request):


    return render(request, 'blog/list.html', {'posts': Post.objects.all()})



#detail view

def detail_view(request, post_pk):


    return render(request, 'blog/detail.html', {'post': Post.objects.get(id = post_pk)})



# update view

def update_view(request, post_pk):

    if request.method == 'POST':
        obj = PostForm(request.POST, instance = Post.objects.get(id = post_pk))
        if obj.is_valid():
            obj.save()
            return redirect('home-path')

    return render(request, 'blog/update.html', {'form' : PostForm(instance = Post.objects.get(id = post_pk))})



# delete view

def delete_view(request, post_pk):



    obj = Post.objects.get(id = post_pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home-path')
    return render(request, 'blog/delete.html', {'post' : Post.objects.get(id = post_pk) })