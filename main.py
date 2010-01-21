# encoding: utf-8

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import handlers

def main():
    urls = (
        ('/', handlers.MainPageHandler),
    )
    run_wsgi_app(webapp.WSGIApplication(urls, debug=True))

if __name__ == "__main__":
    main()
