import random

from django.core.management.base import BaseCommand

from faker import Faker

from faker.generator import random

from polls.models import Author, Publisher, Book, Store


class Command(BaseCommand):
    help = 'informations'

    def handle(self, *args, **kwargs):

        faker = Faker(["ru_RU"])

        auth_list = []
        for i in range(100):
            auth_list.append(Author(name=faker.name(), age=faker.pyint(min_value=20, max_value=80, step=1)))
        Author.objects.bulk_create(auth_list)
        author_ids = Author.objects.values_list("id", flat=True)

        pub_list = []
        for i in range(1000):
            pub_list.append(Publisher(name=faker.company()))
        Publisher.objects.bulk_create(pub_list)
        publishers_ids = Publisher.objects.values_list("id", flat=True)

        books_lsit = []
        for i in range(1000):
            books_lsit.append(
                Book(
                    name=faker.text(max_nb_chars=15),
                    pages=faker.pyint(min_value=20, max_value=1000, step=1),
                    price=faker.pydecimal(right_digits=2, positive=True, min_value=20, max_value=1666),
                    rating=faker.pyfloat(right_digits=2, positive=True, min_value=1, max_value=5),
                    publisher_id=random.choice(publishers_ids),
                    pubdate=faker.date())
            )
        Book.objects.bulk_create(books_lsit)
        books_ids = Book.objects.values_list("id", flat=True)


        for book in Book.objects.all():
            book_auth_ids = set([random.choice(author_ids) for _ in range(random.randint(1, 5))])
            book.authors.add(*book_auth_ids)

        store_list = []
        for i in range(1000):
            store_list.append(Store(name=faker.company()))
        Store.objects.bulk_create(store_list)

        for store in Store.objects.all():
            store_book_ids = set([random.choice(books_ids) for _ in range(random.randint(1, 5))])
            store.books.add(*store_book_ids)

        #  print("Success!!, база данных заполнена")
