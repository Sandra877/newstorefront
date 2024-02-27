from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def package_view(request, *args, **kwargs):
    return render(request, 'package.html', {})