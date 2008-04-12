#!/usr/bin/env python

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class RequestHandler(webapp.RequestHandler):        
    def render_template(self, template_file, dictionary = {}):
        if not dictionary.has_key('lang'):
            # TODO load lang from user
            dictionary['lang'] = 'fr'
        template.register_template_library('app.web.templates_filters')
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', template_file)
        self.response.out.write(template.render(path, dictionary))

    def set_cookie(self, key, value):
        self.response.headers['Set-Cookie'] = key + '=' + value + '; path=/;'

    def delete_cookie(self, key):
        self.response.headers['Set-Cookie'] = key + '=; path=/; Max-Age=0;'

    def get_cookies(self):
        self.request.charset = None
        return self.request.cookies
