#!/usr/bin/env python

from app.web.handlers import RequestHandler

class Home(RequestHandler):
    def get(self):
        self.render_template('index.html')

class NotFound(RequestHandler):
    def get(self, page_name):
        self.render_template('404.html', {'page_name': page_name})

