from test_plus import TestCase

from my_library.users.models import User

from ..models import Book, BookBorrow, Library


class BookBorrowListViewTests(TestCase):
    def setUp(self):
        self.librarian = User.objects.create(name='Librarian',
                                             email='librarian@test.com',
                                             is_superuser=True)
        self.library = Library.objects.create(address='Test address',
                                              librarian=self.librarian)
        self.user = User.objects.create(name='Tester', email='tester@test.com')
        self.url = self.reverse('library:book_borrow_list',
                                user_id=self.user.id)

    def test_with_several_books_borrowed_by_one_user(self):
        book1 = Book.objects.create(
            library=self.library,
            title='Test Title 1',
            description='asdf'
        )
        book2 = Book.objects.create(
            library=self.library,
            title='Test Title 2',
            description='asdf'
        )
        book3 = Book.objects.create(
            library=self.library,
            title='Test Title 3',
            description='asdf'
        )
        book4 = Book.objects.create(
            library=self.library,
            title='Test Title 4',
            description='asdf'
        )
        book5 = Book.objects.create(
            library=self.library,
            title='Test Title 5',
            description='asdf'
        )

        BookBorrow.objects.create(user=self.user, book=book1, charge=1)
        BookBorrow.objects.create(user=self.user, book=book2, charge=1)
        BookBorrow.objects.create(user=self.user, book=book3, charge=1)
        BookBorrow.objects.create(user=self.user, book=book4, charge=1)
        BookBorrow.objects.create(user=self.user, book=book5, charge=1)

        response = self.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, book1.title)
        self.assertContains(response, book2.title)
        self.assertContains(response, book3.title)
        self.assertContains(response, book4.title)
        self.assertContains(response, book5.title)

    def test_with_several_books_borrowed_by_one_user_and_another_user(self):
        another_user = User.objects.create(name='Another user', email='another@test.com')

        user1_book1 = Book.objects.create(
            library=self.library,
            title='Test Title 1',
            description='asdf'
        )
        user1_book2 = Book.objects.create(
            library=self.library,
            title='Test Title 2',
            description='asdf'
        )
        user1_book3 = Book.objects.create(
            library=self.library,
            title='Test Title 3',
            description='asdf'
        )
        user1_book4 = Book.objects.create(
            library=self.library,
            title='Test Title 4',
            description='asdf'
        )
        user1_book5 = Book.objects.create(
            library=self.library,
            title='Test Title 5',
            description='asdf'
        )

        user2_book1 = Book.objects.create(
            library=self.library,
            title='Test Title A',
            description='asdf'
        )
        user2_book2 = Book.objects.create(
            library=self.library,
            title='Test Title B',
            description='asdf'
        )
        user2_book3 = Book.objects.create(
            library=self.library,
            title='Test Title C',
            description='asdf'
        )
        user2_book4 = Book.objects.create(
            library=self.library,
            title='Test Title D',
            description='asdf'
        )
        user2_book5 = Book.objects.create(
            library=self.library,
            title='Test Title F',
            description='asdf'
        )

        BookBorrow.objects.create(user=self.user, book=user1_book1, charge=1)
        BookBorrow.objects.create(user=self.user, book=user1_book2, charge=1)
        BookBorrow.objects.create(user=self.user, book=user1_book3, charge=1)
        BookBorrow.objects.create(user=self.user, book=user1_book4, charge=1)
        BookBorrow.objects.create(user=self.user, book=user1_book5, charge=1)

        BookBorrow.objects.create(user=another_user, book=user2_book1, charge=1)
        BookBorrow.objects.create(user=another_user, book=user2_book2, charge=1)
        BookBorrow.objects.create(user=another_user, book=user2_book3, charge=1)
        BookBorrow.objects.create(user=another_user, book=user2_book4, charge=1)
        BookBorrow.objects.create(user=another_user, book=user2_book5, charge=1)

        response = self.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, user1_book1.title)
        self.assertContains(response, user1_book2.title)
        self.assertContains(response, user1_book3.title)
        self.assertContains(response, user1_book4.title)
        self.assertContains(response, user1_book5.title)

        self.assertNotContains(response, user2_book1.title)
        self.assertNotContains(response, user2_book2.title)
        self.assertNotContains(response, user2_book3.title)
        self.assertNotContains(response, user2_book4.title)
        self.assertNotContains(response, user2_book5.title)
