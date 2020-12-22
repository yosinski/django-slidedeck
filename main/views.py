import os

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.urls import reverse

from main.models import Slidedeck
from util.helper import DuckStruct
import slidedeck.settings as settings



def index(request):
    slidedecks = Slidedeck.objects.all().filter(active = True).order_by('order')

    return render(request,
                  'main/index.html',
                  {'slidedecks': slidedecks})


def about(request):
    return render(request,
                  'main/about.html')


def slides(request, slug):
    try:
        slidedeck = Slidedeck.objects.get(slug = slug)
    except Slidedeck.DoesNotExist:
        raise Http404

    return render(request,
                  'main/slides.html',
                  {'slidedeck': slidedeck})


def fake500(request):
    raise Exception('Fake Error')


def handler404(request):
    return HttpResponseNotFound(render_to_string('main/404.html',
                                                 request=request))


def handler500(request):
    return HttpResponseServerError(render_to_string('main/500.html',
                                                    request=request))
