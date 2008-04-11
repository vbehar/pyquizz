#!/usr/bin/env python

import os
from google.appengine.ext.webapp import template

def render_template(requestHandler, template_file, dictionary = {}):
    path = os.path.join(os.path.dirname(__file__), 'templates', template_file)
    requestHandler.response.out.write(template.render(path, dictionary))
