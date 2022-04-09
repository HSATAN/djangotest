from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import test2
# Create your views here.

def index(request):
    #ip = request.META['HTTP_X_FORWARDED_FOR']
    ip = request.META['REMOTE_ADDR']
    print(ip)
    context = {"data":test2.objects.all(),
               "IP":ip
               }
    return HttpResponse(render(request,'firstapp/index.html', context))
def test(request):
    return HttpResponse("这是test   url")
def month(request, month):
    id1 = get_object_or_404(test2, id=month)
    return render(request,'firstapp/index.html', {'id':id1})

def year(request,month, year):
    return HttpResponse("%d  %d" %(month, year))

def insertuser(request):

    user = test2(user="")
    pass