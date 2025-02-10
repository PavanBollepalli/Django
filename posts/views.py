# from django.shortcuts import render

# # Create your views here.
# def posts_list(request):
#     return render(request,'posts/posts_list.html')
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Posts
from .serializers import PostSerializer

# GET & POST API
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT & DELETE API for a Single Student
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PostSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
