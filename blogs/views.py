from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


def blog_list(request):
    # returns list of blogs
    latest_blogs = Blog.objects.order_by('-date')
    return render(request, 'blog_list.html', dict(blogs = latest_blogs,))

def blog_detail(request, blog_id):
    # returns a detail view of a blog
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', dict(blog = blog,))

def blog_create(request):
    # returns a form for creating a new blog
    error = ""
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            new_form = Blog.objects.create(
                title = form.cleaned_data.get('title'),
                description = form.cleaned_data.get('description')
            )
            new_form.save()
            return redirect(blog_list)
        else:
            error = "Invalid data"
    else:
        form = BlogForm()
    return render(request, 'blog_create.html', dict(form = form, error = error))

def blog_update(request, blog_id):
    # returns a form with pre-populated data to update a blog
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        # update blog
        blog.title = request.POST.get('title')
        blog.description = request.POST.get('description')
        blog.save()
        return redirect(blog_detail, blog_id=blog.id)
    return render(request, 'blog_update.html', dict(blog=blog,))

