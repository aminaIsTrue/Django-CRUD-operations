from django.shortcuts import render

from .forms import PostForm
from .models import Post
# Create your views here.


#create view
def create_view(request):

    if request.method == 'POST':

        obj = PostForm(request.POST)
        if obj.is_valid():
            obj.save()

    return render(request, 'blog/create.html', {'form' : PostForm()})


#list view

def list_view(request):


    return render(request, 'blog/list.html', {'posts': Post.objects.all()})