#!/usr/bin/env python

from google.appengine.ext import webapp

from app.domain import *
from app.web.request_helper import RequestHelper
from app.web.quizz_helper import QuizzHelper

class New(webapp.RequestHandler):
    def get(self):
        request_helper = RequestHelper(self)
        request_helper.delete_cookie('sa')
        request_helper.render_template('quizz/new.html')

class Intro(webapp.RequestHandler):
    def get(self, quizz_name):
        quizz = Quizz()
        quizz.short_name = quizz_name
        request_helper = RequestHelper(self)
        quizz_helper = QuizzHelper(request_helper, quizz)
        user_id = quizz_helper.get_current_user_uuid()
        template_data = {   'name': quizz_name,
                            'user_id': user_id }
        request_helper.render_template('quizz/intro.html', template_data)

class Question(webapp.RequestHandler):
    def get(self, quizz_name, question):
        quizz = Quizz()
        quizz.short_name = quizz_name
        request_helper = RequestHelper(self)
        quizz_helper = QuizzHelper(request_helper, quizz)
        user_id = quizz_helper.get_current_user_uuid()
        quizz_helper.desactivate_current_user()
        template_data = {   'quizz_name': quizz_name,
                            'question': question,
                            'user_id': user_id }
        request_helper.render_template('quizz/question.html', template_data)

class Answer(webapp.RequestHandler):
    def get(self, quizz_name, question, answer):
        template_data = {   'quizz_name': page_name,
                            'question': question,
                            'answer': answer }
        RequestHelper(self).render_template('quizz/answer.html', template_data)

