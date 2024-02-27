from django.shortcuts import render

# Create your views here.
def article_details_view(request, *args, **kwargs):
    return render(request, 'article_details.html', {})
def article_list_view(request, *args, **kwargs):
    return render(request, 'article_list.html', {})

from django.shortcuts import render, HttpResponse
from .forms import BlogForm

def blog_view(request):

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            return HttpResponse('<p>Info Saved!</p>')
        else:
            return HttpResponse('<p>Info is not Valid</p>')

    else:
        form = BlogForm
        context = {
                'form': form,
        }

        return render(request, 'blog_view.html', context)
   