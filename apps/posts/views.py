from django.db.models import Q
from django.shortcuts import render, redirect

from apps.posts.forms import PostForm, CommentForm
from apps.posts.models import Post, Category


def list_post(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'posts.html', context)

def detail_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()

    context = {'post': post,
               'form': form}

    return render(request, 'detail.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {'category': category}
    return render(request, 'category.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'create.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PostForm()

    context = {'form': form}

    return render(request, 'create.html', context)

def about(request):
    return render(request, 'about.html')


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

    return render(request, 'search.html', {'posts': posts, 'query': query})