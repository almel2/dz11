from django.urls import path
from django.views.decorators.cache import cache_page

from polls import views
from polls.views import authordetail, authorslist, index, bookdetail, booklist, publisherdetail, publisherlist, \
    storegetail, storelist, AuthorCreate, AuthorUpdate, AuthorDelete, AuthorListView, StoreListView

urlpatterns = [
    path("", index, name='home'),

    path('book', booklist, name='book'),
    path('author', authorslist, name='author'),
    path('publisher', publisherlist, name='publisher'),
    path('store', storelist, name='store'),

    path('book_dit/<int:pk>', bookdetail, name='book_detail'),
    path('publishers_dit/<int:pk>', publisherdetail, name='publisher_detail'),
    path('authors_dit/<int:pk>', authordetail, name='authors_detail'),
    path('store_dit/<int:pk>', storegetail, name='store_detail'),


    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),

    path('authors_list/', cache_page(10)(AuthorListView.as_view()), name='authors-list'),
    path('store_list/', cache_page(10)(StoreListView.as_view()), name='store-list')
]
