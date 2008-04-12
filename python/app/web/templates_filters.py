#!/usr/bin/env python

from google.appengine.ext.webapp import template

from app import i18n

register = template.create_template_register()

def translate(value, arg):
    return i18n.translate(value, arg)


register.filter(translate)
