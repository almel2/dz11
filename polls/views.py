from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from polls.models import  Author, Book, Publisher, Store



def index(request):
    return render(request, "polls/home_list.html")


def booklist(request):
    books_query = Book.objects.all()
    return render(request, "polls/book_list.html",
                  context={'book': books_query, })


def bookdetail(request, pk):
    pk = Book.objects.prefetch_related('authors').get(pk=pk)
    return render(request, 'polls/book_deteil.html', context={'pk': pk})


def authorslist(request):
    aut_query = Author.objects.prefetch_related('book_set').all()
    return render(request, "polls/authors_list.html",
                  context={'authors': aut_query})


def authordetail(request, pk):
    pk = Author.objects.prefetch_related('book_set').get(pk=pk)
    return render(request, 'polls/autor_detail.html', context={'pk': pk})


def publisherlist(request):
    pub_query = Publisher.objects.prefetch_related('book_set').all()
    return render(request, "polls/publishers_list.html",
                  context={'publishers': pub_query})


def publisherdetail(request, pk):
    pk = Publisher.objects.prefetch_related('book_set').get(pk=pk)
    return render(request, 'polls/publisher_detail.html', context={'pk': pk})


def storelist(request):
    store_query = Store.objects.prefetch_related('books').all()
    return render(request, "polls/store_list.html",
                  context={'store': store_query})


def storegetail(request, pk):
    pk = Store.objects.prefetch_related('books').get(pk=pk)
    return render(request, 'polls/store_detail.html', context={'pk': pk})




class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'age']
    login_url = '/admin/'


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name', 'age']
    login_url = '/admin/'


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('author')
    login_url = '/admin/'

class AuthorListView(ListView):
    model = Author
    template_name = "polls/authors_class.html"
    queryset = Author.objects.prefetch_related('book_set').all()
    paginate_by = 13








