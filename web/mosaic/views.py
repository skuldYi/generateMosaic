from django.shortcuts import render
from .generate.mosaic import mosaic

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'mosaic/index.html', context)


def draw(request):
    params = request.GET
    width = int(params['width'])
    height = int(params['height'])
    step = int(params['step'])
    mosaic((width, height), step)
    return HttpResponse(dict(request.GET))
