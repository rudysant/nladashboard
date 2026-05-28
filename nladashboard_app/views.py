from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Books
from rest_framework.generics import ListAPIView
from .serializers import BooksSerializer

def home(request):
     book_list = Books.objects.all().values()
     template = loader.get_template('catalogue.html')
     context = {
       'book_list': book_list,
         }
     return HttpResponse(template.render(context, request))

class BooksListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer