#!/usr/bin/python

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print "BASE_DIR:" + BASE_DIR
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'demo1.settings'
os.environ['LANG'] = 'ja_JP.UTF-8'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

