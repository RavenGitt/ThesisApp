from django.shortcuts import render
from .models import Author, Publisher, Book

def search(request):
    query = request.GET.get('q')

    if query:
        authors = Author.objects.filter(name__icontains=query)
        books = Book.objects.filter(title__icontains=query)
        publishers = Publisher.objects.filter(name__icontains=query)
    else:
        authors = []
        books = []
        publishers = []

    return render(request, 'search.html', {'authors': authors, 'books': books, 'publishers': publishers, 'query': query})
