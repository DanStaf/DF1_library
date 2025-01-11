from django.urls import reverse

from rest_framework.test import APITestCase

from libr.models import Author, Book, Reading
from users.models import User

from rest_framework import status


class AuthorManagerTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False,
            is_manager=True
        )
        self.author = Author.objects.create(
            first_name='test_name_1',
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse('libr:author-detail', args=(self.author.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('first_name'), self.author.first_name)

    def test_create(self):
        new_text = 'test_name_2'
        url = reverse('libr:author-list')
        data = {
            'first_name': new_text
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)
        self.assertEqual(Author.objects.get(first_name=new_text).first_name, new_text)

    def test_update(self):
        new_text = 'test_author_updated'
        url = reverse('libr:author-detail', args=(self.author.pk,))
        data = {'first_name': new_text}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), new_text)

    def test_delete(self):

        url = reverse('libr:author-detail', args=(self.author.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)

    def test_list(self):
        url = reverse('libr:author-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class AuthorReaderTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False,
            is_manager=False
        )
        self.author = Author.objects.create(
            first_name='test_name_1',
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse('libr:author-detail', args=(self.author.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('first_name'), self.author.first_name)

    def test_create(self):
        new_text = 'test_name_2'
        url = reverse('libr:author-list')
        data = {
            'first_name': new_text
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)
        self.assertEqual(Author.objects.get(first_name=new_text).first_name, new_text)

    def test_update(self):
        new_text = 'test_author_updated'
        url = reverse('libr:author-detail', args=(self.author.pk,))
        data = {'first_name': new_text}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_delete(self):

        url = reverse('libr:author-detail', args=(self.author.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_list(self):
        url = reverse('libr:author-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class BookManagerTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False,
            is_manager=True
        )
        self.author = Author.objects.create(
            first_name='test_name_1',
        )
        self.book = Book.objects.create(
            title='test_title_1',
            year=1990,
            genre='test'
        )
        self.book.authors.add(self.author)
        self.book.save()

        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse('libr:book-detail', args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.book.title)

    def test_create(self):
        new_text = 'test_title_2'
        new_year = 2025
        url = reverse('libr:book-list')
        data = {
            'title': new_text,
            'year': new_year
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)
        self.assertEqual(Book.objects.get(title=new_text).year, new_year)

    def test_update(self):
        new_text = 'test_book_updated'
        url = reverse('libr:book-detail', args=(self.book.pk,))
        data = {'title': new_text}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), new_text)

    def test_delete(self):

        url = reverse('libr:book-detail', args=(self.book.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)

    def test_delete_author(self):

        url = reverse('libr:author-detail', args=(self.author.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)
        self.assertEqual(Book.objects.all().count(), 1)
        self.assertEqual(self.book.authors.count(), 0)

    def test_list(self):
        url = reverse('libr:book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class BookReaderTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False,
            is_manager=False
        )
        self.author = Author.objects.create(
            first_name='test_name_1',
        )
        self.book = Book.objects.create(
            title='test_title_1',
            year=1990,
            genre='test'
        )
        self.book.authors.add(self.author)
        self.book.save()

        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse('libr:book-detail', args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.book.title)

    def test_create(self):
        new_text = 'test_title_2'
        new_year = 2025
        url = reverse('libr:book-list')
        data = {
            'title': new_text,
            'year': new_year
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)
        self.assertEqual(Book.objects.get(title=new_text).year, new_year)

    def test_update(self):
        new_text = 'test_book_updated'
        url = reverse('libr:book-detail', args=(self.book.pk,))
        data = {'title': new_text}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_delete(self):

        url = reverse('libr:book-detail', args=(self.book.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_delete_author(self):

        url = reverse('libr:author-detail', args=(self.author.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_list(self):
        url = reverse('libr:book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ReadingManagerTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False,
            is_manager=True
        )
        self.author = Author.objects.create(
            first_name='test_name_1',
        )
        self.book = Book.objects.create(
            title='test_title_1',
            year=1990,
            genre='test'
        )
        self.book.authors.add(self.author)
        self.reading = Reading.objects.create(
            book=self.book,
            user=self.user
        )
        self.book.save()

        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse('libr:reading-detail', args=(self.reading.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('book'), self.reading.book.pk)

    def test_create(self):

        new_book = Book.objects.create(
            title='test_title_2'
        )

        url = reverse('libr:reading-list')
        data = {
            'book': new_book.pk,
            'user': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reading.objects.all().count(), 2)

    def test_update(self):
        new_text = 'test_updated'
        url = reverse('libr:reading-detail', args=(self.reading.pk,))
        data = {'is_returned': True}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('is_returned'), True)

    def test_delete(self):

        url = reverse('libr:reading-detail', args=(self.reading.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reading.objects.all().count(), 0)

    def test_delete_book(self):

        url = reverse('libr:book-detail', args=(self.book.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)
        self.assertEqual(Reading.objects.all().count(), 0)

    def test_list(self):
        url = reverse('libr:reading-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ReadingReaderTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user_reader@test_user.ru',
            first_name='test_user_reader',
            last_name='test_user_reader',
            is_staff=False,
            is_superuser=False,
            is_manager=False
        )
        self.author = Author.objects.create(
            first_name='test_name_1',
        )
        self.book = Book.objects.create(
            title='test_title_1',
            year=1990,
            genre='test'
        )
        self.book.authors.add(self.author)
        self.reading = Reading.objects.create(
            book=self.book,
            user=self.user
        )
        self.book.save()

        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse('libr:reading-detail', args=(self.reading.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_create(self):

        new_book = Book.objects.create(
            title='test_title_2'
        )

        url = reverse('libr:reading-list')
        data = {
            'book': new_book.pk,
            'user': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_update(self):
        new_text = 'test_updated'
        url = reverse('libr:reading-detail', args=(self.reading.pk,))
        data = {'is_returned': True}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_delete(self):

        url = reverse('libr:reading-detail', args=(self.reading.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_delete_book(self):

        url = reverse('libr:book-detail', args=(self.book.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed

    def test_list(self):
        url = reverse('libr:reading-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not allowed
