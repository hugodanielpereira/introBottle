from os import pardir
from bottle import get, post, delete, run


@get('/')
def index():
    return 'Welcome to bottle!'


@post('/')
def index_post():
    return 'Welcome from POST to Bottle project!'


@delete('/')
def index_delete():
    return 'Welcom from DELETE to bottle project!'


run(host='localhost', port=8080, debug=True)
