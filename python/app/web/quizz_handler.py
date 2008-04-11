#!/usr/bin/env python

from google.appengine.ext import webapp

from app.domain import *
from lib import uuid

class New(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('new quizz<br />')
        self.response.out.write('test uuid : %s' % (uuid.uuid4()))

class Intro(webapp.RequestHandler):
    def get(self, quizz_name):
        q = Quizz()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Quizz name :  %s<br />' % (quizz_name))

class Question(webapp.RequestHandler):
    def get(self, quizz_name, question):
        q = Quizz()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Quizz name :  %s<br />' % (quizz_name))
        self.response.out.write('question :  %s<br />' % (question))

class Answer(webapp.RequestHandler):
    def get(self, quizz_name, question, answer):
        q = Quizz()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Quizz name :  %s<br />' % (quizz_name))
        self.response.out.write('question :  %s<br />' % (question))
        self.response.out.write('answer :  %s<br />' % (answer))


