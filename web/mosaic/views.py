from django.shortcuts import render
from .generate.mosaic import mosaic

# Create your views here.
from django.http import HttpResponse

def convert_color(str):
    rgb = (str[1:3], str[3:5], str[5:7])
    rgb = map(lambda s: int(s, 16), rgb)
    return tuple(rgb)


def index(request):
    context = {}
    return render(request, 'mosaic/index.html', context)


def draw(request):
    try:
        params = request.GET
        width = int(params['width'])
        height = int(params['height'])
        step = int(params['step'])
        color = convert_color(params['color'])

        img = mosaic((width, height), step, color)
        return HttpResponse(img, content_type="image/png")

    except Exception as e:
        return HttpResponse(str(e))
