from app import app
from controllers import ads, works, auth, users, mediums


app.register_blueprint(works.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')

app.register_blueprint(ads.router, url_prefix='/api')

app.register_blueprint(users.router, url_prefix='/api')

app.register_blueprint(mediums.router, url_prefix='/api')
