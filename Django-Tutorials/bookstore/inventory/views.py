from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

# Create your views here.
def book_list(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books, 'query': query})

def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'inventory/book_details.html', {'book': book}) 

