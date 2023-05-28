from django.shortcuts import render, redirect
from .forms import FolderForm, TextForm
from .models import Folder, Text
from django.http import HttpResponseRedirect
import openai
import os
import textwrap
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local, prepare_image_web, draw_boundary, draw_boundary_normalized
import sys

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_file_vision_ai_demo.json'
openai.api_key = "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"

def reset_data(request):
    try:
        Folder.objects.all().delete()
        Text.objects.all().delete()
        return HttpResponseRedirect('/')
    except Exception as e:
        return HttpResponseRedirect(str(e))

def main_page(request):
    try:
        folders = Folder.objects.all()
        texts = Text.objects.all()
        return render(request, 'main_page.html', {'folders': folders, 'texts': texts})
    except Exception as e:
        return render(request, 'main_page.html', {'e': str(e)})

def add_folder(request):
    try:
        if request.method == "POST":
            form = FolderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main_page')
        else:
            form = FolderForm()
        return render(request, 'add_folder.html', {'form': form})
    except Exception as e:
        return render(request, 'add_folder.html', {'e': str(e)})

def add_text(request):
    try:
        client = vision.ImageAnnotatorClient()
        image_file_path = './images/20230523.jpg'
        image = prepare_image_local(image_file_path)
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
                    "role": "system",
                    "content": "The professor is trying to briefly explain the contents of this book to college students",
                },
                {
                    "role": "user",
                    "content": f"{message}\n" + "Summarize in Korean.",
                },
            ],
        )
        long_text = completion.choices[0].message["content"]
        # result = textwrap.fill(long_text, width=50)
        if request.method == "POST":
            form = TextForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main_page')
        else:
            form = TextForm(initial={'content': long_text})
        return render(request, 'add_text.html', {'form': form})
    except Exception as e:
        return render(request, 'add_text.html', {'e': str(e)})

def text_detail(request, text_id):
    try:
        text = Text.objects.get(pk=text_id)
        return render(request, 'text_detail.html', {'text': text})
    except Exception as e:
        return render(request, 'text_detail.html', {'e': str(e)})

def update_text(request, text_id):
    try:
        instance = Text.objects.get(pk=text_id)
        if request.method == "POST":
            form = TextForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('text_detail', text_id=instance.id)
        else:
            form = TextForm(instance=instance)
        return render(request, 'update_text.html', {'form': form})
    except Exception as e:
        return render(request, 'update_text.html', {'e': str(e)})

def delete_text(request, text_id):
    try:
        text = Text.objects.get(pk=text_id)
        text.delete()
        return redirect('main_page')
    except Exception as e:
        return render(request, 'main_page.html', {'e': str(e)})