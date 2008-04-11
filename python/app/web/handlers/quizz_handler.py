#!/usr/bin/env python

from app.domain import *
from app.web.handlers import RequestHandler
from app import util

class QuizzHandler(RequestHandler):
    def get_current_user_uuid(self, quizz_short_name):
        cookies = self.get_cookies()
        if cookies.has_key(quizz_short_name):
            return cookies.get(quizz_short_name)
        else:
            user_uuid = util.generate_uuid()
            self.set_cookie(quizz_short_name, user_uuid)
            return user_uuid

    def desactivate_current_user(self, quizz_short_name):
        self.delete_cookie(quizz_short_name)


class New(QuizzHandler):
    def get(self):
        self.render_template('quizz/new.html')

class Intro(QuizzHandler):
    def get(self, quizz_short_name):
        quizz = Quizz()
        user_id = self.get_current_user_uuid(quizz_short_name)
        template_data = {   'name': quizz_short_name,
                            'user_id': user_id }
        self.render_template('quizz/intro.html', template_data)

class Question(QuizzHandler):
    def get(self, quizz_short_name, question):
        quizz = Quizz()
        user_id = self.get_current_user_uuid(quizz_short_name)
        self.desactivate_current_user(quizz_short_name)
        template_data = {   'quizz_name': quizz_short_name,
                            'question': question,
                            'user_id': user_id }
        self.render_template('quizz/question.html', template_data)

class Answer(QuizzHandler):
    def get(self, quizz_short_name, question, answer):
        template_data = {   'quizz_name': quizz_short_name,
                            'question': question,
                            'answer': answer }
        self.render_template('quizz/answer.html', template_data)

