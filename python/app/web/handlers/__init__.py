#!/usr/bin/env python

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from app.domain import *
from app import i18n

class RequestHandler(webapp.RequestHandler):
    def render_template(self, template_file, dictionary = {}):
        if not dictionary.has_key('lang'):
            # load lang from user prefs => make user a class attribute ?
            # otherwise, fallback to the lang from the request headers :
            dictionary['lang'] = i18n.choose_lang(self.request.accept_language.best_matches(i18n.DEFAULT_LANG))
        template.register_template_library('app.web.templates_filters')
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', template_file)
        self.response.out.write(template.render(path, dictionary))

    def get_current_user(self, quizz_short_name):
        user_uuid = __get_current_user_uuid(quizz_short_name)
        user = User.get_or_insert(key_name=user_uuid)
        if user.uuid == None:
            user.uuid = user_uuid
            user.lang = i18n.choose_lang(self.request.accept_language.best_matches(i18n.DEFAULT_LANG))
        return user

    def get_current_quizz(self, quizz_short_name):
        quizz = Quizz.get_by_key_name(key_name=quizz_short_name)
        if quizz == None:
            self.redirect('/404')
        return quizz

    def get_current_question(self, quizz, question_id):
        query = Question.all()
        query.filter('quizz = ', quizz)
        query.filter('id = ', question_id)
        question = query.get()
        if question == None:
            self.redirect('/404')
        return question

    def desactivate_current_user(self, quizz_short_name):
        self.__delete_cookie(quizz_short_name)

    # private methods

    def __get_current_user_uuid(self, quizz_short_name):
        cookies = self.__get_cookies()
        if cookies.has_key(quizz_short_name):
            return cookies.get(quizz_short_name)
        else:
            user_uuid = util.generate_uuid()
            self.__set_cookie(quizz_short_name, user_uuid)
            return user_uuid

    def __set_cookie(self, key, value):
        self.response.headers['Set-Cookie'] = key + '=' + value + '; path=/;'

    def __delete_cookie(self, key):
        self.response.headers['Set-Cookie'] = key + '=; path=/; Max-Age=0;'

    def __get_cookies(self):
        self.request.charset = None
        return self.request.cookies
