#!/usr/bin/env python

from google.appengine.ext import webapp

from app.domain import *
from lib import uuid

class New(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('new quizz<br />')
        self.response.out.write('test uuid : %s' % (uuid.uuid4()))

class View(webapp.RequestHandler):
    def get(self, quizz_name):
        q = Quizz()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Quizz name :  %s' % (quizz_name))

