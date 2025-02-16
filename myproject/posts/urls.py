from django.urls import path
from .views import posts_list,posts_page
app_name="posts"
urlpatterns = [
    path('', posts_list, name="list"),
    path('<slug:slug>', posts_page, name="page"),
]
