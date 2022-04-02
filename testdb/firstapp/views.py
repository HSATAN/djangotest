from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print()
    return HttpResponse("黄浪波你是个棒槌")