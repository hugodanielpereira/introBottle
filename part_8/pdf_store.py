from bottle import run, route, template, get, post, request, static_file
import os


@route('/')
def index():
    return template('index', uploads=os.listdir(r'.\\uploads'))


@get('/upload')
def upload():
    return ''' <form action="/upload" method="post" enctype="multipart/form-data" action="__URL__">
    <!-- MAX_FILE_SIZE must precede the file input field -->
    <input type="hidden" name="MAX_FILE_SIZE" value="30000" />
    <!-- Name of input element determines name in $_FILES array -->
    Select a file: <input type="file" name="upload" />
    <input type="submit" value="Start upload" />
    </form> '''


@post('/upload')
def upload():
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)

    if not ext in ('.jpg', '.png', '.pdf', '.jpeg'):
        return 'You are not allowed to upload file: {} with the extension {}'.format(name, ext)

    path = r'.\\uploads'
    upload.save(path, overwrite=True)
    return 'OK'


@route('/uploads/<file>')
def show(file):
    return static_file(file, root=r'.\\uploads')


run(host='localhost', port=8080, reloader=True, debug=True)
