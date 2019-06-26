import os
from app import app
from controllers import ads, works, auth, users, mediums


app.register_blueprint(works.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')

app.register_blueprint(ads.router, url_prefix='/api')

app.register_blueprint(users.router, url_prefix='/api')

app.register_blueprint(mediums.router, url_prefix='/api')


@app.route('/') # homepage
@app.route('/<path:path>') # any other path
def catch_all(path='index.html'):

    if os.path.isfile('dist/' + path): # if path is a file, send it back
        return app.send_static_file(path)

    return app.send_static_file('index.html') # otherwise send back the index.html file
