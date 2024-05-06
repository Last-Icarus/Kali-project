from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

def login_page(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')


@api_view(['GET', 'POST'])
def page_list(request):
    if request.method == 'GET':
        data = Page.objects.all()
        serializer = PageSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('post')
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)