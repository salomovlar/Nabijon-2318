from django.shortcuts import render
from django.http import JsonResponse
from books.models import Book

def index(request):
    books = Book.objects.all()
    total = books.count()
    sold = books.filter(sold=True).count()
    available = total - sold
    return render(request, 'index.html', {
        'books': books,
        'total': total,
        'sold': sold,
        'available': available
    })

def katalog(request):
    books = Book.objects.all()
    return render(request, 'katalog.html', {'books': books})

def buyurtma(request):
    return render(request, 'buyurtma.html')

def biz_haqimizda(request):
    return render(request, 'biz-haqimizda.html')

def api_books(request):
    books = Book.objects.all()
    data = list(books.values('name', 'author', 'price', 'sold'))
    return JsonResponse(data, safe=False)
