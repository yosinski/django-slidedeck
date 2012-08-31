import os

from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from util.helper import DuckStruct
import settings



def index(request):
    return render_to_response('main/index.html',
                              context_instance = RequestContext(request))



def fake500(request):
    raise Exception('Fake Error')

def handler404(request):
    return HttpResponseNotFound(render_to_string('main/404.html',
                                                 context_instance = RequestContext(request)))

def handler500(request):
    return HttpResponseServerError(render_to_string('main/500.html',
                                                    context_instance = RequestContext(request)))
