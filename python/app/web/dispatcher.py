#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp

from app.web.handlers import default_handler
from app.web.handlers import quizz_handler

def main():
    application = webapp.WSGIApplication([
            ('/', default_handler.Home),
            ('/404', default_handler.NotFound),
            ('/403', default_handler.NotAuthorized),
            ('/new-quizz', quizz_handler.New),
            (r'/quizz/(.*)/(.*)/(.*)', quizz_handler.Answer),
            (r'/quizz/(.*)/(.*)', quizz_handler.Question),
            (r'/quizz/(.*)', quizz_handler.Intro),
            (r'/(.*)', default_handler.NotFound)
        ],
        debug=True
    )
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
