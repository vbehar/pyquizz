#!/usr/bin/env python

import os
import sys
import yaml

AVAILABLE_LANGS = [
    'fr',
    'en'
]

DEFAULT_LANG = 'fr'

_translations = {}

def load_translations():
    for lang in AVAILABLE_LANGS:
        translation_file = os.path.join(os.path.dirname(__file__), 'translation_' + lang + '.yaml')
        _translations[lang] = yaml.load(file(translation_file, 'r').read())

load_translations()

def translate(key, lang = DEFAULT_LANG):
    # FIXME : remove me for prod (only use in DEV to auto-reload .yaml files)
    load_translations()
    if not lang in AVAILABLE_LANGS:
        lang = DEFAULT_LANG
    if not _translations[lang].has_key(key):
        return key
    return _translations[lang][key]
