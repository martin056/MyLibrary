import uuid

from djmoney.models.fields import MoneyField

from django.db import models
from django.utils import timezone

from ..users.models import User


class Library(models.Model):
    address = models.CharField(max_length=255)
    librarian = models.OneToOneField(User, related_name='library', on_delete=models.CASCADE)


class Book(models.Model):
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)

    public_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class BookBorrow(models.Model):
    book = models.ForeignKey(Book, related_name='book_borrows', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='book_borrows', on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    charge = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    returned = models.BooleanField(default=False)

    class Meta:
        unique_together = ('book', 'user', 'start_date', )
