#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp

from app.web import default_handler
from app.web import quizz_handler

def main():
    application = webapp.WSGIApplication([
                                        ('/', default_handler.Home),
                                        ('/new-quizz', quizz_handler.New),
                                        (r'/quizz/(.*)/(.*)/(.*)', quizz_handler.Answer),
                                        (r'/quizz/(.*)/(.*)', quizz_handler.Question),
                                        (r'/quizz/(.*)', quizz_handler.Intro),
                                        (r'/(.*)', default_handler.NotFound)],
                                        debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
