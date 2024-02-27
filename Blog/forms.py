from django.forms import ModelForm
from .models import blog

class BlogForm(ModelForm):

    class Meta:
        model = blog
        fields = ['title','details', 'blogs']