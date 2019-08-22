from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
# Create your views here


def index(request):
    s = 'List of publications\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('published'):    # minus stands for desc order
        s += bb.published.strftime('%d%m%Y %H-%M') + '\r\n' + bb.title + '\r\n' + bb.content + '\r\n\r\n'

    return HttpResponse(s, content_type='text/plain', charset='utf-8')

