# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter
import urllib
from django import utils

register = template.Library()

@register.filter(name='unenc')
@stringfilter
def unenc(value):
    #print "unenc encode('utf8'):%s" % type(value.encode('utf8'))
    print "unenc: %s %s" % (type(value), value)
    ret =  urllib.unquote(value.encode('utf8'))
    print "unenc ret %s %s" % (type(ret), ret)
    return ret


