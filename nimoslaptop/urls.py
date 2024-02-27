from .views  import package_view
from django.urls import path

app_name = 'package'
urlpatterns = [
    path('', package_view, name='package_view')
]
