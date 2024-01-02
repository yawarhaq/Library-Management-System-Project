from django.contrib import admin
from django.urls import path
from .views import HelloLMS, AddbookView, Adddata, EditbookView, Editbook, DeletebookView, issue_book


urlpatterns = [
    path("", HelloLMS),
    path("add_book", AddbookView),
    path("add_book/add", Adddata),
    path("edit_book/", EditbookView),
    path("edit_book/edit", Editbook),
    path("delete_book/", DeletebookView),
    path('issue_book/', issue_book, name='issue_book'),
]