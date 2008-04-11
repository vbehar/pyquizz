#!/usr/bin/env python

from google.appengine.ext import webapp

from app.web import *

class Home(webapp.RequestHandler):
    def get(self):
        render_template(self, 'index.html')

class NotFound(webapp.RequestHandler):
    def get(self, page_name):
        render_template(self, '404.html', {'page_name':page_name})

