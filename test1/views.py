# -*- coding: utf-8 -*-
# Create your views here.

import sys,os
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response ,get_object_or_404
from django.template import RequestContext,Context, loader
import urllib
from django import utils
import forms

def index(request):
    print "index() called"
    pi = request.path_info.encode('utf8')
    pi_enc =  utils.http.urlquote(pi).encode('utf8')
    print "index pi:%s %s" % (type(pi), pi)
    print "index pi_enc:%s %s" % (type(pi_enc), pi_enc)
    return render_to_response('test1/index.html', {'pi':pi, 'pi_enc':pi_enc})


def download(request):
    print "download() called"
    f1 = '/home/yoyama/data1.jpg'
    file_size = os.path.getsize(f1)
    print file_size
    response = HttpResponse(open(f1, 'rb').read(), mimetype="application/octet-stream")
    #response['Content-Disposition'] = 'attachment; filename="%s";' % os.path.basename(f1).upper()
    response['Content-Disposition'] = 'attachment; filename="%s";' % os.path.basename(f1)
    response['Content-Length'] = '%d' % file_size
    response['Content-Transfer-Encoding'] = 'binary';
    return response


@csrf_protect
def upload(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.POST['name'])
            return HttpResponseRedirect('/top/')
        else:
            folder = ""
            if(request.GET.has_key('folder')):
                folder = request.GET['folder']
            c['form'] = form
            c['folder'] = folder
            return render_to_response('test1/upload.html', c)

    else:
        print c
        form = forms.UploadFileForm()
        folder = ""
        if(request.GET.has_key('folder')):
            folder = request.GET['folder']
        print form
        c['form'] = form
        c['folder'] = folder
        return render_to_response('test1/upload.html', c)


def handle_uploaded_file(f, n):
    with open('/tmp/'+ n.encode('utf8'), 'wb+') as fo:
        for chunk in f.chunks():
            fo.write(chunk)






