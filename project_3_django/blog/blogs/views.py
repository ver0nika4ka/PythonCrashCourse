from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """Home page for Blog."""
    return render(request, 'blogs/index.html')

def blogposts(request):
    """Show all blogposts on the page."""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)

def blogpost(request, blogpost_id):
    """Show one post on the page."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    context = {'blogpost': blogpost}
    return render(request, 'blogs/blogpost.html', context)

def new_post(request):
    """Add a new blogpost."""
    if request.method != 'POST':
        # if GET - create a blank form for new post.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogposts')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request,'blogs/new_post.html', context)

def edit_post(request, blogpost_id):
    """Edit existing blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        # If GET, pre-fill form with the current post.
        form = BlogPostForm(instance=blogpost)
    else:
        # POST data submitted, process data.
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost.id)

    context = {'blogpost': blogpost, 'form': form} 
    return render(request,'blogs/edit_post.html', context)





