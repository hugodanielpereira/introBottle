from unicodedata import name
from bottle import run, route, template, view


@route('/')
@view('hello_template')
def index():
    return dict(name='Stranger')


run(host='localhost', port=8080, debug=True)
