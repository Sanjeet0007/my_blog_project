# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog' # Used for namespacing URLs

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/',
         views.post_detail,
         name='post_detail'),
]