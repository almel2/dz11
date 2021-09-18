from random import randrange

from django.core.management.base import BaseCommand
from faker import Faker

import faker.providers
from faker.generator import random

from polls.models import Author, Publisher, Book, Store

author = [
    "И. Северянин"
    "Н .А. Клюев"
    "Б. К. Зайцев"
    "В. Хлебников"
    "А. В. Дружинин"
    "А. Б. Мариенгоф"
    "А. Ф. Писемский"
    "Р. Ивнев"
    "Н. Г. Помяловский"
]


class Provider(faker.providers.BaseProvider):
    def ecommerce_category(self):
        return self.random_element(author)


class Command(BaseCommand):
    help = 'informations'

    def handle(self, *args, **kwargs):

        faker = Faker(["ru_RU"])

        for i in range(100):
            Author(name=faker.name(), age=faker.pyint(min_value=20, max_value=80, step=1)).save()

        for i in range(100):
            Publisher(name=faker.company()).save()

        for i in range(100):
            publisher = Publisher.objects.get(pk=random.randint(1, 100))
            authors_id = random.randint(1, 100)
            book_id = random.randint(1, 100)
            Book.objects.create(
                name=faker.text(max_nb_chars=15),
                pages=faker.pyint(min_value=20, max_value=1000, step=1),
                price=faker.pydecimal(right_digits=2, positive=True, min_value=20, max_value=1666),
                rating=faker.pyfloat(right_digits=2, positive=True, min_value=1, max_value=5),
                publisher=publisher,
                pubdate=faker.date())

        for i in range(100):
            Book.objects.get(pk=book_id).authors.add(Author.objects.get(pk=authors_id))

        for i in range(100):
            Store(name=faker.company()).save()
        for i in range(100):
            stor_id = random.randint(1, 100)
            book_id = random.randint(1, 100)
            Store.objects.get(pk=stor_id).books.add(Book.objects.get(pk=book_id))

        #  print("Success!!, база данных заполнена")
