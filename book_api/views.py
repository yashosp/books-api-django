from django.shortcuts import render
from book_api.models import Book
from django.http import JsonResponse
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
# views(Logic) can be class or function

# to return the list of books
@api_view(['GET'])
def books_list(request):
    books = Book.objects.all() # datatype as Complex data
    serializer = BookSerializer(books, many=True) # many list of objects into JSOn
    return Response(serializer.data) # converting python DS to JSON

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)                                        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)

# show, delete, update a specific record using unique id
# /books/1

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except:
        return Response({'error': 'Book does not exists'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book.delete()
        return Response({'Deleted': True})