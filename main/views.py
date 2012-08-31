import os

from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from main.models import Slidedeck
from util.helper import DuckStruct
import settings



def index(request):
    slidedecks = Slidedeck.objects.all().order_by('order')

    return render_to_response('main/index.html',
                              {'slidedecks': slidedecks},
                              context_instance = RequestContext(request))



def slides(request, slug):
    try:
        slidedeck = Slidedeck.objects.get(slug = slug)
    except Slidedeck.DoesNotExist:
        raise Http404

    return render_to_response('main/slides.html',
                              {'slidedeck': slidedeck},
                              context_instance = RequestContext(request))



def fake500(request):
    raise Exception('Fake Error')

def handler404(request):
    return HttpResponseNotFound(render_to_string('main/404.html',
                                                 context_instance = RequestContext(request)))

def handler500(request):
    return HttpResponseServerError(render_to_string('main/500.html',
                                                    context_instance = RequestContext(request)))
