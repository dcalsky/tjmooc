from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .models import Homework, HomeworkSubmit, Test, TestSubmit
from .serializer import HomeworkSerializer, HomeworkSubmitSerializer, TestSerializer, TestSubmitSerializer
from rest_framework.views import APIView

class HomeworkList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        homework = Homework.objects.all()
        serializer = HomeworkSerializer(homework, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class HomeworkDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        try:
            return Homework.objects.get(id=id)
        except Homework.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        homework = self.get_object(id)
        serializer = HomeworkSerializer(homework)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id, format=None):
        homework = self.get_object(id)
        serializer = HomeworkSerializer(homework, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        homework = self.get_object(id)
        homework.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HomeworkSubmitList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        homework_submit = HomeworkSubmit.objects.all()
        serializer = HomeworkSubmitSerializer(homework_submit, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = HomeworkSubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class HomeworkSubmitkDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        try:
            return HomeworkSubmit.objects.get(id=id)
        except HomeworkSubmit.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        homework_submit = self.get_object(id)
        serializer = HomeworkSubmitSerializer(homework_submit)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id, format=None):
        homework_submit = self.get_object(id)
        serializer = HomeworkSubmitSerializer(homework_submit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        homework_submit = self.get_object(id)
        homework_submit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








class TestkList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TestkDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        try:
            return Test.objects.get(id=id)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        test = self.get_object(id)
        serializer = TestSerializer(test)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id, format=None):
        test = self.get_object(id)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        test = self.get_object(id)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TestSubmitList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        test_submit = TestSubmit.objects.all()
        serializer = TestSubmitSerializer(test_submit, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TestSubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TestSubmitkDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        try:
            return TestSubmit.objects.get(id=id)
        except TestSubmit.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        test_submit = self.get_object(id)
        serializer = TestSubmitSerializer(test_submit)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id, format=None):
        test_submit = self.get_object(id)
        serializer = TestSubmitSerializer(test_submit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        test_submit = self.get_object(id)
        test_submit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)