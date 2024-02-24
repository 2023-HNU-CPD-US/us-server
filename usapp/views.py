from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, Http404, HttpResponse
from django.conf import settings
from .models import Folder, Text, Image
import openai
import os
import sys
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local, prepare_image_web, draw_boundary, draw_boundary_normalized
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import TextSerializer, FolderSerializer

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_file_vision_ai_demo.json'
openai.api_key = "대충 키 값이였던 것"

class AddText(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        text = Text.objects.all()
        text_serializer = TextSerializer(text, many=True)
        return Response(text_serializer.data)
    def post(self, request):
        file = request.data.get('file')
        if file:
            image = Image(photo=file)
            image.save()
            image_path = image.photo.path
            long_text = analyze(image_path)
            return Response({"result": long_text}, status=status.HTTP_201_CREATED)
        return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

class SaveText(APIView):
    def get(self, request):
        text = Text.objects.all()
        text_serializer = TextSerializer(text, many=True)
        return Response(text_serializer.data)
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def analyze(image_path):
    client = vision.ImageAnnotatorClient()
    image = prepare_image_local(image_path)
    va = VisionAI(client, image)
    message = ""
    texts = va.text_detection()
    for indx, text in enumerate(texts):
        message += text.description
        if indx > 3:
            break
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{message}\n" + "Summarize this content based on the important information to make it easy to read in Korean.",
            },
        ],
    )
    analyzed_text = completion.choices[0].message["content"]
    return analyzed_text

class PutText(APIView):
    def get_object(self, id):
        try:
            print(id)
            return Text.objects.get(id=id)
        except Text.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        text = self.get_object(id)
        serializer = TextSerializer(text)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        text = self.get_object(id)
        serializer = TextSerializer(text, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteText(APIView):
    def get_object(self, id):
        try:
            return Text.objects.get(id=id)
        except Text.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        text = self.get_object(id)
        serializer = TextSerializer(text)
        return Response(serializer.data)
    def delete(self, request, id, format=None):
        text = self.get_object(id)
        text.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddFolder(APIView):
    def get(self, request):
        folder = Folder.objects.all()
        folder_serializer = FolderSerializer(folder, many=True)
        return Response(folder_serializer.data)
    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutFolder(APIView):
    def get_object(self, id):
        try:
            return Folder.objects.get(id=id)
        except Folder.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        folder = self.get_object(id)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        folder = self.get_object(id)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteFolder(APIView):
    def get_object(self, id):
        try:
            return Folder.objects.get(id=id)
        except Folder.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        folder = self.get_object(id)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)
    def delete(self, request, id, format=None):
        folder = self.get_object(id)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class main_page(APIView):
    def get(self, request, format=None):
        text = Text.objects.all()
        text_serializer = TextSerializer(text, many=True)
        folder = Folder.objects.all()
        folder_serializer = FolderSerializer(folder, many=True)
        return Response({
            'text': text_serializer.data,
            'folder': folder_serializer.data
        })
    def my_view(request):
        response = HttpResponse()
        response['Cache-Control'] = 'no-cache'
        return response

class EditName_Text(APIView):
    def get_object(self, id):
        try:
            print(id)
            return Text.objects.get(id=id)
        except Text.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        text = self.get_object(id)
        serializer = TextSerializer(text)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        text = self.get_object(id)
        new_name = request.data.get('name', text.name)
        if new_name:
            text.name = new_name
            text.save()
            serializer = TextSerializer(text)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
