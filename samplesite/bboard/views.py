from django.shortcuts import render

from .models import Bb
# Create your views here


def index(request):

    bbs = Bb.objects.order_by('published')    # minus stands for desc order

    return render(request, 'bboard/index.html', {'bbs': bbs})

