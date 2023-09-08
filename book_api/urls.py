from django.contrib import admin
from django.urls import path
from book_api.views import books_list, book_create, book

urlpatterns = [
    path('list/', books_list),
    path('', book_create),
    path('<int:pk>', book)
]
