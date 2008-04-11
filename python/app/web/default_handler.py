#!/usr/bin/env python

from google.appengine.ext import webapp

class Home(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('homepage')

class NotFound(webapp.RequestHandler):
    def get(self, page_name):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('404 on page :  %s' % (page_name))

