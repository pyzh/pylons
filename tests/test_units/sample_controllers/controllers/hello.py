import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers import WSGIController
from pylons.controllers.util import abort, redirect
from webob import Response
from webob.exc import HTTPNotFound

log = logging.getLogger(__name__)

class HelloController(WSGIController):
    def __init__(self):
        self._pylons_log_debug = True

    def index(self):
        return 'Hello World'
    
    def oops(self):
        raise Exception('oops')
    
    def abort(self):
        abort(404)


def special_controller(environ, start_response):
    return HTTPNotFound()

def empty_wsgi(environ, start_response):
    return
