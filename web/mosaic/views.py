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
    # try:
    params = request.POST
    width = int(params['width'])
    height = int(params['height'])
    step = int(params['step'])
    line_width = int(params['line_width'])
    line_color = params['line_color']
    side = int(params['side'])
    color = convert_color(params['color'])
    pattern = request.FILES.get('image')

    size = {'width': width, 'height': height, 'pixel': side}

    border = {'width': line_width, 'color': line_color}

    img = mosaic(size, step, color, pattern, border)
    return HttpResponse(img, content_type="blob")

# except Exception as e:
#     return HttpResponse(str(e))
