from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# coding:utf-8

def index(request):
    return render(request, 'home.html')

'''
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
'''