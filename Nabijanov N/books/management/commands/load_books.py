import json
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Load books from data.json into database'

    def handle(self, *args, **options):
        with open('data.json', 'r', encoding='utf-8') as f:
            books_data = json.load(f)

        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                name=book_data['name'],
                author=book_data['author'],
                defaults={
                    'price': book_data['price'],
                    'sold': book_data['sold']
                }
            )
            if created:
                self.stdout.write(f"Added: {book.name}")
            else:
                self.stdout.write(f"Already exists: {book.name}")

        self.stdout.write(self.style.SUCCESS('Successfully loaded books from data.json'))
