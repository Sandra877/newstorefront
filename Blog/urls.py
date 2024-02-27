from .views  import article_details_view, article_list_view, blog_view
from django.urls import path

urlpatterns = [
    path('', article_list_view, name='article_list_view'),
    path('', article_details_view, name='article_detail_view'),
    path('blogview/', blog_view, name='blog_view')


]
