from app import app
from controllers import ads, works, auth

app.register_blueprint(ads.router, url_prefix='/api')
app.register_blueprint(works.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')
