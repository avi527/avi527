from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Libraries,Books,Library_books,Users,Library_activites
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from LibraryApp.serializers import BooksSerializer,LibrariesSerializer,LibraryBookRecordSerializer,LibraryBookInOutSerializer
import uuid
# Create your views here.
@api_view(['POST'])
def CreateBook(request):
    '''
    payload:
    {
	"title": "Cool Man",
	"author_name": "MS Dhoni",
	"genre": "Biographical",
	"discription": "All Rounder"
    }
    '''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['isbn_num'] = uuid.uuid4().hex
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def CreateLibraries(request):
    '''
    payload
    {
	"name": "Mahi",
	"city": "Rachi",
	"state": "Jharkhand",
	"postal_code": "843329"
    }

    '''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibrariesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def CreateLibraryBookRecord(request):
    '''
    payload
    {
	"library_id":3,
	"book_id": 13,
    "last_library_activity_id":0
    }
    '''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibraryBookRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def CreateLibraryCheckInOut(request):
    '''
    payload - check In
    {
	"activity_type":"in",
	"user_id": 3,
    "library_book_id":2,
    "checked_in_at": "2021-11-28 15:23:00"
    }
    payload - check Out
    {
	"activity_type":"in",
	"user_id": 3,
    "library_book_id":2,
    "checked_out_at": "2021-11-28 15:23:00"
}
    '''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibraryBookInOutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            Library_books.objects.update(last_library_activity_id=serializer.data['library_activity_id'])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def LibraryBookOutFromUser(request):
    '''
    payload
    {"user_id":3}
    '''
    if request.method == 'GET':
        data = JSONParser().parse(request)
        userId = data['user_id']
        data = Library_activites.objects.filter(user_id=userId,activity_type="out")
        serializer = LibraryBookInOutSerializer(data, many=True)
        return Response(serializer.data, status=200)

@api_view(['GET'])
def AllBookOutFromLib(request):
    '''
    payload
    {"user_id":3}
    '''
    if request.method == 'GET':
        data = Library_activites.objects.filter(activity_type="out")
        serializer = LibraryBookInOutSerializer(data, many=True)
        return Response(serializer.data, status=200)


