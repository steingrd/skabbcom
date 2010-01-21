# encoding: utf-8

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

def render_to_response(handler, template_name, context=None):
    if not context:
        context = {}
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    path = os.path.join(templates_dir, template_name)
    handler.response.out.write(template.render(path, context))