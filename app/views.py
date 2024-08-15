from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def longboat(request):
    return HttpResponse('this is a good pub')