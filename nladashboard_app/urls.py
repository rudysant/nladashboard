from django.urls import path
from . import views
from .views import BooksListView

urlpatterns = [
    path('', views.home, name='home'),
    path('api/books/', BooksListView.as_view(), name='book-list'),

    
]