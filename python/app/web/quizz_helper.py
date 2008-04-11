#!/usr/bin/env python

from app.domain import *
from app import util

class QuizzHelper(object):

    def __init__(self, request_helper, quizz):
        self.request_helper = request_helper
        self.quizz = quizz

    def get_current_user_uuid(self):
        cookies = self.request_helper.get_cookies()
        if cookies.has_key(self.quizz.short_name):
            return cookies.get(self.quizz.short_name)
        else:
            user_uuid = util.generate_uuid()
            self.request_helper.set_cookie(self.quizz.short_name, user_uuid)
            return user_uuid

    def desactivate_current_user(self):
        self.request_helper.delete_cookie(self.quizz.short_name)
