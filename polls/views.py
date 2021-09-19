
from django.shortcuts import render

from polls.models import  Author, Book, Publisher, Store


def index(request):
    return render(request, "polls/home_list.html")


def BookList(request):
    books_query = Book.objects.all()
    return render(request, "polls/book_list.html",
                  context={'books': books_query, })


def BookDetail(request, pk):
    pk = Book.objects.prefetch_related('authors').get(pk=pk)
    return render(request, 'polls/book_deteil.html', context={'pk': pk})


def AuthorsList(request):
    aut_query = Author.objects.prefetch_related('book_set').all()
    return render(request, "polls/authors_list.html",
                  context={'authors': aut_query})


def AuthorDetail(request, pk):
    pk = Author.objects.prefetch_related('book_set').get(pk=pk)
    return render(request, 'polls/autor_detail.html', context={'pk': pk})


def PublisherList(request):
    pub_query = Publisher.objects.prefetch_related('book_set').all()
    return render(request, "polls/publishers_list.html",
                  context={'publishers': pub_query})


def PublisherDetail(request, pk):
    pk = Publisher.objects.prefetch_related('book_set').get(pk=pk)
    return render(request, 'polls/publisher_detail.html', context={'pk': pk})


def StoreList(request):
    store_query = Store.objects.prefetch_related('books').all()
    return render(request, "polls/store_list.html",
                  context={'store': store_query})


def StoreDetail(request, pk):
    pk = Store.objects.prefetch_related('books').get(pk=pk)
    return render(request, 'polls/store_detail.html', context={'pk': pk})
