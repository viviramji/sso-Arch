import os
from flask import Flask

def create_app(test_config=None): 



    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping( 
        Secrect_key = 'dev',
        Database = os.path.join(app.instance_path, 'app2.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'PRIMERA APP YEIIIII!'

    from.import db
    db.init_app(app)

    from.import auth
    app.register_blueprint(auth.bp)

    from.import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app