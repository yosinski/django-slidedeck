from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from django import template

import settings


register = template.Library()


@register.filter
@stringfilter
def stripp(value, arg=None):
    if arg is None:
        return value.strip()
    else:
        return value.strip(arg)



@register.filter
@stringfilter
def header_path_links(value):
    path = value.strip().strip('/')

    link = settings.SITE_URL_BASE.strip('/')
    #print settings.APPEND_SLASH
    ret = ''
    #print 'parts are', repr(path.split('/'))
    for part in path.split('/'):
        link += '/' + part
        #print 'part is', part, 'link is', link
        append = '/' if settings.APPEND_SLASH else ''
        ret += ' / ' + '<a href="%s">%s</a>' % (link + append, part)
    ret = ret[3:]
    return mark_safe(ret)
