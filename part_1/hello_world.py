from bottle import run, route


@route('/')
def index():
    return 'Wellcome to bottle stranger!'


run(host='localhost', port=8080, debug=True)
