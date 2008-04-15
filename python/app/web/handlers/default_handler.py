#!/usr/bin/env python

from app.web.handlers import RequestHandler

class Home(RequestHandler):
    def get(self):
        self.render_template('index.html')

class NotFound(RequestHandler):
    def get(self, page_name):
        template_data = {}
        if page_name != None and page_name != '404':
            template_data['page_name'] = page_name
        self.render_template('404.html', template_data)

class NotAuthorized(RequestHandler):
    def get(self, page_name):
        self.render_template('403.html')

