from django.contrib import admin

from polls.models import *

class BookAuthorInline(admin.StackedInline):
    model = Book.authors.through
    extra = 3


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)
    inlines = [
        BookAuthorInline,
    ]
    ordering = ['name', 'age']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price',)
    list_filter = ('authors', 'publisher',)
    date_hierarchy = 'pubdate'
    fieldsets = (('Book info',
                  {'fields': ('name', 'pages', 'price')}),
                 ('★★★★★', {'fields': ('rating',)}),
                 ('Publisher', {'fields': ('publisher',)}),
                 ('Date', {'fields': ('pubdate',)}))
    inlines = [BookAuthorInline, ]
    ordering = ['name', 'price']
    search_fields = ['name', 'author']


class BookInline(admin.TabularInline):
    model = Book
    max_num = 3


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [BookInline, ]
    ordering = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name']
