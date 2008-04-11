#!/usr/bin/env python

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class RequestHandler(webapp.RequestHandler):        
    def render_template(self, template_file, dictionary = {}):
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', template_file)
        self.response.out.write(template.render(path, dictionary))

    def set_cookie(self, key, value):
        self.response.headers['Set-Cookie'] = key + '=' + value + ';'

    def delete_cookie(self, key):
        self.response.headers['Set-Cookie'] = key + '=; Max-Age=0;'

    def get_cookies(self):
        self.request.charset = None
        return self.request.cookies
