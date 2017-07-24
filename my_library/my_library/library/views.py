from django.shortcuts import render
from django.http import HttpResponseNotAllowed

from .models import BookBorrow


def book_borrow_list(request, user_id):
    if request.method == 'GET':
        object_list = BookBorrow.objects.filter(user__id=user_id)

        return render(request, 'book_borrow_list.html', locals())

    return HttpResponseNotAllowed(['GET'])
