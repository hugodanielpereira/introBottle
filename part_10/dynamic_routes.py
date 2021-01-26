from bottle import run, route, response


@route('/forum')
@route('/forum/<name>')
def forum(name='specifications'):
    return 'You have hit the {} named forum!'.format(name)


@route('/<action>/<username>')
def manager(action, username):
    return 'You have specified action: {} on username {}'.format(action, username)


run(host='localhost', port=8080, reloader=True, debug=True)
