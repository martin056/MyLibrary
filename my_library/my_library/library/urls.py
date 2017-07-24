from django.conf.urls import url

from .views import book_borrow_list


urlpatterns = [
    url(
        regex=r'^(?P<user_id>[0-9]+)/book-borrow-list/$',
        view=book_borrow_list,
        name='book_borrow_list'
    ),
]
