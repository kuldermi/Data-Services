from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = models.Students.objects.all()
        serializer = serializers.StudentSerializer( students , many = True )
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.StudentSerializer( data= request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    try:
        student= models.Students.objects.get(pk = pk)
    except models.Students.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.StudentSerializer( student )
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.StudentSerializer( student , data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = models.Teacher.objects.all()
        serializer = serializers.TeacherSerializer(teachers, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.TeacherSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def teacher_details(request, pk):
    try:
        teacher= models.Teacher.objects.get(pk= pk)
    except models.Teacher.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = serializers.TeacherSerializer(teacher)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.TeacherSerializer(teacher, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


