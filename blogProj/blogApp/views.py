from django.shortcuts import render


# Create your views here.
from blogApp.forms import BlogForm
from blogApp.models import BlogModel


def main_blog_page(request):
    blog = BlogModel.objects.all()
    context = {'blog': blog}
    return render(request, 'main.html', context=context)


def info_show_page(request, pk):
    task = BlogModel.objects.get(pk=pk)
    context = {'task': task}
    return render(request, 'moreInfo.html', context=context)


def create_post_show_page(request):
    blogs = BlogModel.objects.all()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            count = form.cleaned_data['count']

            BlogModel.objects.create(user_id=user_id,
                                     author=author,
                                     title=title,
                                     text=text,
                                     count=count)
            context = {'form': form,
                       'blogs': blogs}
            return render(request, 'createPost.html', context=context)
        else:
            context = {'form': form,
                       'blogs': blogs}
            return render(request, 'createPost.html', context=context)
    else:
        form = BlogForm(request.POST)
        context = {'form': form,
                   'blogs': blogs}
        return render(request, 'createPost.html', context=context)
