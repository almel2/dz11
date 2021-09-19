from django.urls import path

from polls.views import AuthorDetail, AuthorsList, index, BookDetail, BookList, PublisherDetail, PublisherList, \
    StoreDetail, StoreList

urlpatterns = [
    path("", index, name='home'),

    path('book', BookList, name='book'),
    path('author', AuthorsList, name='author'),
    path('publisher', PublisherList, name='publisher'),
    path('store', StoreList, name='store'),

    path('book_dit/<int:pk>', BookDetail, name='book_detail'),
    path('publishers_dit/<int:pk>', PublisherDetail, name='publisher_detail'),
    path('authors_dit/<int:pk>', AuthorDetail, name='authors_detail'),
    path('store_dit/<int:pk>', StoreDetail, name='store_detail')
]
