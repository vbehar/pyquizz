#!/usr/bin/env python

import os

from google.appengine.ext.webapp import template

class RequestHelper(object):

    def __init__(self, request_handler):
        self.request_handler = request_handler

    def render_template(self, template_file, dictionary = {}):
        path = os.path.join(os.path.dirname(__file__), 'templates', template_file)
        self.request_handler.response.out.write(template.render(path, dictionary))

    def set_cookie(self, key, value):
        self.request_handler.response.headers['Set-Cookie'] = key + '=' + value + ';'

    def delete_cookie(self, key):
        self.request_handler.response.headers['Set-Cookie'] = key + '=; Max-Age=0;'

    def get_cookies(self):
        self.request_handler.request.charset = None
        return self.request_handler.request.cookies
