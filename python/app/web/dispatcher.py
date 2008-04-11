#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp

from app.web import quizz_handler

def main():
    application = webapp.WSGIApplication([
                                        ('/', quizz_handler.New),
                                        (r'/quizz/(.*)', quizz_handler.View)],
                                        debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
