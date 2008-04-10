#!/usr/bin/env python

import os
import sys

DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

EXTRA_PATHS = [
  DIR_PATH,
  os.path.join(DIR_PATH, 'app', 'domain'),
  os.path.join(DIR_PATH, 'app', 'web'),
  os.path.join(DIR_PATH, 'app', 'util'),
  os.path.join(DIR_PATH, 'lib')
]

APP_DISPATCHER_PATH = 'app/web/dispatcher.py'

if __name__ == '__main__':
  sys.path = EXTRA_PATHS + sys.path
  script_path = os.path.join(DIR_PATH, APP_DISPATCHER_PATH)
  execfile(script_path, globals())

