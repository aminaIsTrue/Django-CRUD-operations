from django.shortcuts import render

from .forms import PostForm
from .models import Post
# Create your views here.


#create view
def create_view(request):


    return render(request, 'blog/create.html', {'form' : PostForm()})