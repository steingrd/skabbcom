# encoding: utf-8

from google.appengine.ext import webapp

from shortcuts import render_to_response

class MainPageHandler(webapp.RequestHandler):    
    def get(self):
        return render_to_response(self, 'main.html')
        