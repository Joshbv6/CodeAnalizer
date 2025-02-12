from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django import forms
from git import Repo
import os, traceback
from CodeAnalizer.classes.repositories import Repository

def home(request):
    return render(request, 'home.html')

def sast_form(request):
    return render(request, 'sast.html')

def repository_sast(request):
    if request.method == "POST":
        repository = Repository(request)
        if repository.url:
            try:
                repo_results = repository.clone_repository()
        
                return render(request, "repository.html", {"results": repo_results})
                        

            except Exception as e:
                tb = traceback.extract_tb(e.__traceback__)
                filename, line, func, text = tb[-1] 
                error_message = mark_safe("The server had issues cloning that!<br>Could you check the URL and try again?")
                return render(request, "repository.html", {"error": error_message})
        else:
            return render(request, "repository.html", {"error": "URL is required"})