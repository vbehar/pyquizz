#!/usr/bin/env python

from google.appengine.ext import webapp

from app.domain import *
from app import util
from app.web import *

class New(webapp.RequestHandler):
    def get(self):
        render_template(self, 'quizz/new.html')

class Intro(webapp.RequestHandler):
    def get(self, quizz_name):
        q = Quizz()
        render_template(self, 'quizz/intro.html',  {'name':quizz_name,
                                                    'user_id': util.generate_uuid()})

class Question(webapp.RequestHandler):
    def get(self, quizz_name, question):
        render_template(self, 'quizz/question.html',    {'quizz_name':page_name,
                                                        'question':question})

class Answer(webapp.RequestHandler):
    def get(self, quizz_name, question, answer):
        render_template(self, 'quizz/answer.html', {'quizz_name':page_name,
                                                    'question':question,
                                                    'answer':answer})


